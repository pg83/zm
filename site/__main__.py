import jinja2

import libs.py_resource as lp


def get_source(name):
    print(name)

    return lp.load(name).decode('utf-8'), name, lambda: True


env = jinja2.Environment(loader=jinja2.FunctionLoader(get_source))

print(env.get_template('/index.html').render(variable='Value with <unsafe> data', item_list=[1, 2, 3, 4, 5, 6]))
