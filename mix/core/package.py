import os
import sys
import json
import hashlib


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
        return self.mix_dir + '/workdir/' + self.uid

    @property
    def src_dir(self):
        return self.out_dir + '-src'

    def depends(self):
        return self._d['build'].get('depends', [])

    def iter_depends(self):
        for d in self.depends():
            yield self.manager.load_package(d)

    def iter_env(self):
        path = ['/nowhere']

        for p in self.iter_depends():
            yield p.name.replace('-', '_'), p.out_dir

            path.append(p.out_dir)

        yield 'PATH', ':'.join(path)

    def iter_full_env(self):
        yield from self.iter_env()

        yield 'out', self.out_dir
        yield 'src', self.src_dir
        yield 'tmp', self.tmp_dir

    def iter_src_env(self):
        yield from self.iter_env()

        yield 'out', self.src_dir
        yield 'tmp', self.tmp_dir

    def build_sh_script(self, data, env):
        return {
            'args': ['/bin/sh', '-s'],
            'stdin': BUILD_SH_SCRIPT.format(build_script=data),
            'env': env,
        }

    def build_py_script(self, data, env, args=[]):
        return {
            'args': [sys.executable, self.manager.binary, 'misc', 'runpy'] + args,
            'stdin': BUILD_PY_SCRIPT.format(build_script=data),
            'env': env,
        }

    def build_script(self):
        by_kind = {
            'sh': self.build_sh_script,
            'py': self.build_py_script,
        }

        build = self._d['build']['script']

        return by_kind[build.kind](build.data, dict(self.iter_full_env()))

    def fetch_src_script(self):
        urls = [x['url'] for x in self._d['build']['fetch']]

        return self.build_py_script(FETCH_SRC_SCRIPT, dict(self.iter_src_env()), urls)

    def iter_commands(self):
        yield {
            'out': [self.src_dir + '/touch'],
            'cmd': [self.fetch_src_script()],
        }

        yield {
            'in': [x.out_dir + '/touch' for x in self.iter_depends()] + [self.src_dir + '/touch'],
            'out': [self.out_dir + '/touch'],
            'cmd': [self.build_script()],
        }

    def commands(self):
        return list(self.iter_commands())
