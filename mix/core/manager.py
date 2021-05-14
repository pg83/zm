import os

import core.utils as cu
import core.package as cp


class Manager:
    def __init__(self, binary, where):
        self._b = binary
        self._w = where
        self._c = {}

    @property
    def mix_dir(self):
        return os.path.expanduser('~/mix')

    @property
    def binary(self):
        return self._b

    @property
    def where(self):
        return self._w

    def load_package(self, name):
        if name not in self._c:
            self._c[name] = cp.Package(os.path.join(self.where, name), self)

        return self._c[name]

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
