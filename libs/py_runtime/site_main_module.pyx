import site_res_wrapper as srs


for k in srs.keys():
    if k.endswith('__main__.py'):
        path = k[5:]
        code = compile(srs.value_by_key(k), path, 'exec')

        glob = {
            '__name__': __name__,
            '__file__': path,
        }

        exec(code, glob)

import importlib.util
