import site_res_wrapper as srs

__file__ = '__main__.py'

exec(compile(srs.value_by_key('/_py/' + __file__), __file__, 'exec'))
