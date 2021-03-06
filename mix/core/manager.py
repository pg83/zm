import os

import core.j2 as cj
import core.utils as cu
import core.package as cp


class Manager:
    def __init__(self, binary, where):
        self._b = binary
        self._w = where
        self._c = {}
        self._e = cj.Env(where)

    @property
    def env(self):
        return self._e

    @property
    @cu.cached_method
    def mix_dir(self):
        return os.path.expanduser('~/mix')

    @property
    def binary(self):
        return self._b

    @property
    def where(self):
        return self._w

    def load_file(self, path):
        with open(os.path.join(self.where, path)) as f:
            return f.read()

    def load_package(self, name):
        while True:
            try:
                return self._c[name]
            except KeyError:
                pass

            self._c[name] = cp.Package(name, self)

    def iter_packages(self, names):
        def iter_deps():
            for name in names:
                yield name
                yield from self.load_package(name).all_depends()

        for d in cu.iter_uniq_list(iter_deps()):
            yield self.load_package(d)

    def iter_build_commands(self, names):
        for pkg in self.iter_packages(names):
            yield from pkg.commands()

    def build_graph(self, names):
        return {
            'nodes': list(self.iter_build_commands(names)),
            'targets': [self.load_package(x).out_dir + '/touch' for x in names],
        }

    def all_packages(self):
        w = self.where

        for a, b, c in os.walk(w):
            for x in c:
                if x == 'package.py':
                    yield self.load_package(a[len(w) + 1:])
