import json
import jinja2
import bottle

import libs.py_resource as lp


class Iface:
    def __init__(self):
        d = {}

        for k in lp.keys():
            if k.startswith('/site/'):
                d[k[6:]] = lp.load(k)

        self._d = d

    def data(self, name):
        return self._d[name]

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
@app.route('/templates/<name>')
def templates(name='index.html'):
    return env.get_template('templates/' + name).render(iface=iface)


@app.route('/static/<name>')
def templates(name):
    return iface.data('static/' + name)


if __name__ == '__main__':
    bottle.run(app, host='localhost', port=8080)
