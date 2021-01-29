module: library

depends:
- tp/libs/python/src

inc_dirs:
- tp/libs/python/src/Include

srcs:
- site_import_hook.pyx
- site_main_module.pyx
