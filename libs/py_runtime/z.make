module: library

depends:
- tp/libs/python/src
- libs/resource

inc_dirs:
- libs/py_runtime

srcs:
- site_import_hook.pyx
- site_res_wrapper.pyx
- wrapper.cpp
