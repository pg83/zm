import sys
import traceback
import site_res_wrapper as srw

sys.excepthook = traceback.print_exception
sys.abiflags = ''

__file__ = '__main__.py'

exec(compile(srw.value_by_key('/_py/' + __file__), __file__, 'exec'))
