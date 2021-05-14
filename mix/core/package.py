import os
import sys
import json
import hashlib

import core.utils as cu


class File:
    def __init__(self, name, data):
        self.name = name
        self.data = data

    @property
    def kind(self):
        return self.name.split('.')[-1]

    def __json__(self):
        return {
            'kind': self.kind,
            'data': self.data,
        }


class FileLoader:
    def __init__(self, where):
        self._w = where

    def __getattr__(self, name):
        path = os.path.join(self._w, name.replace('_', '.'))

        with open(path, 'r') as f:
            return File(os.path.basename(path), f.read())


def exec_mod(text, iface):
    g = {}

    exec(text, g)

    return g['package'](iface)


def string_hash(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


def struct_hash(d):
    return string_hash(json.dumps(d, sort_keys=True, default=lambda x: x.__json__()))


BUILD_SH_SCRIPT = '''
set -e
set -x
set -u

(rm -rf $out || 1) && mkdir -p $out
(rm -rf $tmp || 1) && mkdir -p $tmp

cd $tmp

{build_script}

rm -rf $tmp
touch $out/touch
'''.strip()


BUILD_PY_SCRIPT = '''
import os
import shutil

def prepare_dir(d):
    try:
        shutil.rmtree(d)
    except FileNotFoundError:
        pass

    os.makedirs(d)

out = os.environ['out']
tmp = os.environ['tmp']

prepare_dir(out)
prepare_dir(tmp)

os.chdir(tmp)

{build_script}

shutil.rmtree(tmp)

with open(out + '/touch', 'w') as f:
    pass
'''.strip()


FETCH_SRC_SCRIPT = '''
import os
import sys

for url in sys.argv[1:]:
    mix.fetch_url(url, os.path.join(os.environ['out'], os.path.basename(url)))
'''.strip()


BUILD_PSH_SCRIPT = '''
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
        self._d = exec_mod(self.files.package_py.data, self)
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
    def files(self):
        return FileLoader(self.where)

    @property
    def uid(self):
        return self._u

    @property
    def mix_dir(self):
        return self.manager.mix_dir

    @property
    def out_dir(self):
        return self.mix_dir + '/store/' + self.uid + '-' + self.name

    @property
    def tmp_dir(self):
        return self.mix_dir + '/tmp/build/' + self.uid

    @property
    def src_dir(self):
        return self.mix_dir + '/tmp/fetch/' + struct_hash(self._d['build']['fetch'])

    def depends(self):
        return self._d['build'].get('depends', [])

    def all_depends(self):
        def iter_deps():
            for d in self.depends():
                yield d

                yield from self.manager.load_package(d).all_depends()

        return cu.uniq_list(iter_deps())

    def iter_all_depends(self):
        for d in self.all_depends():
            yield self.manager.load_package(d)

    def iter_env(self):
        path = ['/nowhere']

        for p in self.iter_all_depends():
            yield p.name.replace('-', '_'), p.out_dir

            path.append(p.out_dir + '/bin')

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

    def build_psh_script(self, data, env, args=[]):
        return {
            'args': [sys.executable, self.manager.binary, 'misc', 'runpsh'] + args,
            'stdin': BUILD_PSH_SCRIPT.format(build_script=data),
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
            'psh': self.build_psh_script,
        }

        build = self._d['build']['script']

        return by_kind[build.kind](build.data, dict(self.iter_env()))

    def fetch_src_script(self):
        def iter_env():
            yield from self.iter_env()

            yield 'out', self.src_dir
            yield 'tmp', self.tmp_dir

        urls = [x['url'] for x in self._d['build']['fetch']]

        return self.build_py_script(FETCH_SRC_SCRIPT, dict(iter_env()), urls)

    def iter_commands(self):
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
            'in': [x.out_dir + '/touch' for x in self.iter_all_depends()] + extra,
            'out': [self.out_dir + '/touch'],
            'cmd': [self.build_script()],
        }

    def commands(self):
        return list(self.iter_commands())
