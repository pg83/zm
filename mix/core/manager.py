import os
import getpass

import core.package as cp


class Manager:
    def __init__(self, binary, where):
        self._b = binary
        self._w = where
        self._c = {}

    @property
    def mix_dir(self):
        return os.path.join(getpass.getuser(), 'mix')

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
        v = set()

        def visit(name):
            if name not in v:
                v.add(name)

                pkg = self.load_package(name)

                yield pkg

                for n in pkg.depends():
                    yield from visit(n)

        for name in names:
            yield from visit(name)

    def iter_build_commands(self, names):
        for pkg in self.iter_packages(names):
            yield from pkg.commands()

    def build_graph(self, names):
        return {
            'nodes': list(self.iter_build_commands(names)),
            'targets': [self.load_package(x).out_dir + '/touch' for x in names],
        }
