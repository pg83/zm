module: program

namespace: top_level

srcs:
- __main__.py

resource:
- site/templates/site.html
- site/templates/index.html
- site/data/items.json

depends:
- tp/libs/python/lib
- tp/libs/jinja2
- tp/libs/bottle
- libs/py_main
- libs/py_resource
