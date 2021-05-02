module: program

namespace: top_level

srcs:
- __main__.py

resource:
- index.html /index.html

depends:
- tp/libs/python/lib
- tp/libs/jinja2
- libs/py_main
- libs/py_resource
