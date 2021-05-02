module: program

namespace: top_level

srcs:
- __main__.py

resource:
- site/site.html site.html
- site/index.html index.html
- site/items.json items.json

depends:
- tp/libs/python/lib
- tp/libs/jinja2
- tp/libs/bottle
- libs/py_main
- libs/py_resource
