import json
import jinja2
import bottle

import libs.py_resource as lp


class Iface:
    def data(self, name):
        return lp.load('/' + name)

    def text(self, name):
        return self.data(name).decode('utf-8')

    def json(self, name):
        return json.loads(self.text(name))

    def source(self, name):
        return self.text(name), name, lambda: True


iface = Iface()
env = jinja2.Environment(loader=jinja2.FunctionLoader(iface.source))
app = bottle.Bottle()


@app.route('/')
@app.route('/<name>')
def route(name='index.html'):
    return env.get_template('index.html').render(iface=iface)


bottle.run(app, host='localhost', port=8080)
