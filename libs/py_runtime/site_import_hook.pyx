import sys

from _frozen_importlib import spec_from_loader
from _io import FileIO


def file_bytes(path):
    # 'open' is not avaiable yet.
    with FileIO(path, 'r') as f:
        return f.read()


where = '/Users/pg/zm/tp/libs/python/src/Lib'
#sys.dont_write_bytecode = True
#sys.path.append(where)


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
        path = where + '/' + fullname.replace('.', '/') + '.py'

        return file_bytes(path), path

    def get_code(self, fullname):
        try:
            data, path = self.get_source(fullname)
        except:
            data, path = self.get_source(fullname + '.__init__')

        return compile(data, path, 'exec')

    def is_package(self, fullname):
        try:
            self.get_source(fullname)

            return False
        except:
            pass

        try:
            self.get_source(fullname + '.__init__')

            return True
        except:
            pass

        raise ImportError(fullname)


sys.meta_path.insert(0, Finder())
