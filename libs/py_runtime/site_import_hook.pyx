import sys

from _frozen_importlib import spec_from_loader

import site_res_wrapper as srw


def fmt(*args):
    sys.stderr.write(' '.join([str(x) for x in args]))


class Finder(object):
    def find_spec(self, fullname, path, target=None):
        try:
            is_package = self.is_package(fullname)
        except ImportError:
            return None

        return spec_from_loader(fullname, self, is_package=is_package)

    def create_module(self, spec):
        return None

    def find_module(self, fullname, path=None):
        spec = self.find_spec(fullname, path)

        return spec.loader if spec is not None else None

    def exec_module(self, module):
        code = self.get_code(module.__name__)
        module.__file__ = code.co_filename
        exec(code, module.__dict__)

    def get_source(self, fullname):
        return srw.from_utf8(self.get_data(fullname)[0])

    def get_src(self, fullname):
        path = fullname.replace('.', '/') + '.py'

        return srw.value_by_key('/_py/' + path), path

    def get_data(self, fullname):
        try:
            return self.get_src(fullname)
        except KeyError:
            return self.get_src(fullname + '.__init__')

    def get_code(self, fullname):
        data, path = self.get_data(fullname)

        return compile(data, path, 'exec', dont_inherit=True)

    def is_package(self, fullname):
        try:
            self.get_src(fullname)

            return False
        except:
            pass

        try:
            self.get_src(fullname + '.__init__')

            return True
        except:
            pass

        raise ImportError(fullname)


sys.meta_path.insert(0, Finder())
