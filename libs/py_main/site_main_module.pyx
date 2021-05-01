import sys
import traceback
import site_res_wrapper as srw

sys.excepthook = traceback.print_exception
sys.abiflags = ''

g = {
    '__file__': '__main__.py',
    '__name__': '__main__',
}

exec(compile(srw.value_by_key('/_py/' + g['__file__']), g['__file__'], 'exec'), g)
