import os
import sys
import json
import hashlib

import core.utils as cu


class FileLoader:
    def __init__(self, where):
        self._w = where

    def __getattr__(self, name):
        path = os.path.join(self._w, name.replace('_', '.'))

        with open(path, 'r') as f:
            return {
                'kind': os.path.basename(path).split('.')[-1],
                'data': f.read(),
            }


def exec_mod(text, iface):
    g = {}

    exec(text, g)

    return g['package'](iface)


def string_hash(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


def struct_hash(d):
    return string_hash(json.dumps(d, sort_keys=True))


BUILD_SH_SCRIPT = '''
set -e
set -x

(rm -rf "$out" || 1) && mkdir -p "$out"
(rm -rf "$tmp" || 1) && mkdir -p "$tmp"

cd "$tmp"

echo "$PATH" | tr ':' '\n' | tac | while read p; do
    env=$(realpath -m "$p/../env")

    if test -f "$env"; then
        cat "$env" >> "$tmp/tmpenv"
    fi
done

. "$tmp/tmpenv" && rm "$tmp/tmpenv" && env

{build_script}

rm -rf "$tmp"
touch "$out/touch"
'''.strip()


BUILD_PY_SCRIPT = '''
mix.header()

{build_script}

mix.footer()
'''.strip()


FETCH_SRC_SCRIPT = '''
import os
import sys

for url in sys.argv[1:]:
    mix.fetch_url(url, os.path.join(os.environ['out'], os.path.basename(url)))
'''.strip()


BUILD_PH_SCRIPT = '''
newdir $out
newdir $tmp

cd $tmp

{build_script}

rm $tmp
touch $out/touch
'''.strip()


class Package:
    def __init__(self, where, mngr):
        self._w = where
        self._m = mngr
        self._d = exec_mod(self.files.package_py['data'], self)
        self._u = struct_hash([self._d, list(self.iter_env())])

    @property
    def manager(self):
        return self._m

    @property
    def name(self):
        return os.path.basename(self.where)

    @property
    def where(self):
        return self._w

    @property
    @cu.cached_method
    def files(self):
        return FileLoader(self.where)

    @property
    def uid(self):
        return self._u

    @property
    def mix_dir(self):
        return self.manager.mix_dir

    @property
    @cu.cached_method
    def out_dir(self):
        return self.mix_dir + '/store/' + self.uid + '-' + self.name

    @property
    @cu.cached_method
    def tmp_dir(self):
        return self.mix_dir + '/tmp/build/' + self.uid

    @property
    @cu.cached_method
    def src_dir(self):
        return self.mix_dir + '/tmp/fetch/' + struct_hash(self._d['build']['fetch'])

    # build
    def build_depends(self):
        return self._d.get('build', {}).get('depends', [])

    @cu.cached_method
    def all_build_depends(self):
        def iter_deps():
            yield from self.build_depends()

            for d in self.build_depends():
                yield from self.manager.load_package(d).all_runtime_depends()

        return cu.uniq_list(iter_deps())

    def iter_all_build_depends(self):
        for d in self.all_build_depends():
            yield self.manager.load_package(d)

    # runtime
    def runtime_depends(self):
        return self._d.get('runtime', {}).get('depends', [])

    @cu.cached_method
    def all_runtime_depends(self):
        def iter_deps():
            yield from self.runtime_depends()

            for d in self.runtime_depends():
                yield from self.manager.load_package(d).all_runtime_depends()

        return cu.uniq_list(iter_deps())

    def iter_all_runtime_depends(self):
        for d in self.all_runtime_depends():
            yield self.manager.load_package(d)

    # all
    def depends(self):
        return self.build_depends() + self.runtime_depends()

    @cu.cached_method
    def all_depends(self):
        def iter_deps():
            for d in self.depends():
                yield d
                yield from self.manager.load_package(d).all_depends()

        return cu.uniq_list(iter_deps())

    def iter_env(self):
        path = ['/nowhere']

        for p in self.iter_all_build_depends():
            od = p.out_dir

            yield p.name.replace('-', '_'), od

            path.append(od + '/bin')

        yield 'PATH', ':'.join(path)

    def build_sh_script(self, data, env):
        return {
            'args': ['dash', '-s'],
            'stdin': BUILD_SH_SCRIPT.format(build_script=data),
            'env': env,
        }

    def build_py_script(self, data, env, args=[]):
        return {
            'args': [sys.executable, self.manager.binary, 'misc', 'runpy'] + args,
            'stdin': BUILD_PY_SCRIPT.format(build_script=data),
            'env': env,
        }

    def build_ph_script(self, data, env, args=[]):
        return {
            'args': [sys.executable, self.manager.binary, 'misc', 'runph'] + args,
            'stdin': BUILD_PH_SCRIPT.format(build_script=data),
            'env': env,
        }

    def build_script(self):
        def iter_env():
            yield from self.iter_env()

            if 'fetch' in self._d['build']:
                yield 'src', self.src_dir

            yield 'out', self.out_dir
            yield 'tmp', self.tmp_dir
            yield 'mix', self.manager.binary

            yield 'exe', sys.executable

        by_kind = {
            'sh': self.build_sh_script,
            'py': self.build_py_script,
            'ph': self.build_ph_script,
        }

        build = self._d['build']['script']

        return by_kind[build['kind']](build['data'], dict(iter_env()))

    def fetch_src_script(self):
        def iter_env():
            yield from self.iter_env()

            yield 'out', self.src_dir
            yield 'tmp', self.tmp_dir

        urls = [x['url'] for x in self._d['build']['fetch']]

        return self.build_py_script(FETCH_SRC_SCRIPT, dict(iter_env()), urls)

    def iter_commands(self):
        if 'build' not in self._d:
            yield {
                'out': [self.out_dir + '/touch'],
                'cmd': [self.build_ph_script('', dict(out=self.out_dir, tmp=self.tmp_dir))],
            }

            return

        if 'fetch' in self._d['build']:
            touch = self.src_dir + '/touch'

            yield {
                'out': [touch],
                'cmd': [self.fetch_src_script()],
            }

            extra = [touch]
        else:
            extra = []

        yield {
            'in': [x.out_dir + '/touch' for x in self.iter_all_build_depends()] + extra,
            'out': [self.out_dir + '/touch'],
            'cmd': [self.build_script()],
        }

    def commands(self):
        return list(self.iter_commands())
