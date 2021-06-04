import os
import sys
import json
import base64
import jinja2
import hashlib
import multiprocessing

import core.utils as cu


class FileLoader:
    def __init__(self, pkg):
        self._p = pkg

    def __getattr__(self, name):
        path = os.path.join(self._p.where, name.replace('_', '.'))

        with open(path, 'r') as f:
            data = f.read()
            tmpl = jinja2.Template(data, keep_trailing_newline=True).render(mix=self._p)

            return {
                'kind': os.path.basename(path).split('.')[-1],
                'data': tmpl,
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

(rm -rf "$out" || true) && mkdir -p "$out"
(rm -rf "$tmp" || true) && mkdir -p "$tmp"

cd "$tmp" && echo > tmpenv

echo "$PATH" | tr ':' '\n' | tac | while read p; do
    env=$(realpath -m "$p/../env")

    if test -f "$env"; then
        cat "$env" >> "$tmp/tmpenv"
    fi
done

. "$tmp/tmpenv" && rm "$tmp/tmpenv"

set -x

{build_script}

set +x

rm -rf $out/lib/*.so* || true
rm -rf $out/lib/*.la* || true
rm -rf $out/lib/*.dylib* || true

rm -rf "$tmp"
'''.strip()


BUILD_PY_SCRIPT = '''
mix.header()

{build_script}

mix.footer()
'''.strip()


FETCH_SRC_SCRIPT = '''
import sys

mix.fetch_url(sys.argv[1], sys.argv[2])
mix.check_md5(sys.argv[2], sys.argv[3])
'''.strip()


LINK_SRCS_SCRIPT = '''
import sys
import os

os.chdir(os.environ['out'])

for f in sys.argv[1:]:
    os.link(f, os.path.basename(f))
'''.strip()


BUILD_PH_SCRIPT = '''
newdir $out
newdir $tmp

cd $tmp

{build_script}

rm $tmp
'''.strip()


class Package:
    def __init__(self, name, mngr):
        self._n = name
        self._m = mngr
        self._d = exec_mod(self.files.package_py['data'], self)
        self._u = struct_hash([self._d, list(self.iter_env())])

    def base64(self, data):
        return base64.b64encode(data.encode('utf-8')).decode('utf-8')

    @property
    def manager(self):
        return self._m

    @property
    def name(self):
        return self._n

    @property
    def where(self):
        return os.path.join(self.manager.where, self.name)

    @property
    @cu.cached_method
    def files(self):
        return FileLoader(self)

    @property
    def uid(self):
        return self._u

    @property
    def mix_dir(self):
        return self.manager.mix_dir

    @property
    @cu.cached_method
    def out_dir(self):
        return self.mix_dir + '/store/' + self.uid + '-' + self.name.replace('/', '-')

    @property
    @cu.cached_method
    def tmp_dir(self):
        return self.mix_dir + '/build/' + self.uid

    def src_dir_for(self, url):
        return self.mix_dir + '/fetch/' + struct_hash(url)

    @property
    def src_dir(self):
        return self.src_dir_for(self._d['build']['fetch'])

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

            yield p.name.replace('-', '_').replace('/', '_'), od

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

            yield 'make_thrs', str(multiprocessing.cpu_count() + 2)

        build = self._d['build']['script']

        return {
            'sh': self.build_sh_script,
            'py': self.build_py_script,
            'ph': self.build_ph_script,
        }[build['kind']](build['data'], dict(iter_env()))

    def fetch_src_script(self, url, md5):
        path = os.path.join(self.src_dir_for([url, md5]), os.path.basename(url))

        def iter_env():
            yield from self.iter_env()

            yield 'out', os.path.dirname(path)

        return self.build_py_script(FETCH_SRC_SCRIPT, dict(iter_env()), [url, path, md5])

    def empty_script(self):
        return self.build_py_script('', dict(out=self.out_dir))

    def empty_command(self):
        script = self.empty_script()

        return {
            'out_dir': [script['env']['out']],
            'cmd': [script],
        }

    def link_srcs_script(self, files, out):
        def iter_env():
            yield from self.iter_env()

            yield 'out', out

        return self.build_py_script(LINK_SRCS_SCRIPT, dict(iter_env()), files)

    def iter_commands(self):
        if 'build' not in self._d:
            yield self.empty_command()

            return

        extra = []

        for ui in self._d['build'].get('fetch', []):
            script = self.fetch_src_script(ui['url'], ui.get('md5', ''))
            path = script['args'][-2]

            cmd = {
                'out_dir': [os.path.dirname(path)],
                'cmd': [script],
                'path': path,
            }

            yield cmd

            extra.append(cmd)

        if extra:
            script = self.link_srcs_script([x['path'] for x in extra], self.src_dir)

            cmd = {
                'in_dir': sum([x['out_dir'] for x in extra], []),
                'out_dir': [script['env']['out']],
                'cmd': [script],
            }

            yield cmd

            extra = cmd['out_dir']

        yield {
            'in_dir': [x.out_dir for x in self.iter_all_build_depends()] + extra,
            'out_dir': [self.out_dir],
            'cmd': [self.build_script()],
        }

    def commands(self):
        return list(self.iter_commands())
