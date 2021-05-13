import os
import sys
import subprocess

import urllib.request as ur


class Iface:
    def fetch_url(self, url, out):
        print('fetch ' + url + ' into ' + out)

        try:
            self.fetch_curl(url, out)
        except FileNotFoundError:
            self.fetch_urllib(url, out)

    def fetch_curl(self, url, out):
        subprocess.check_call(['curl', '--output', out, url])

    def fetch_urllib(self, url, out):
        import ssl

        ssl._create_default_https_context = ssl._create_unverified_context

        data = ur.urlopen(url).read()

        with open(out, 'wb') as f:
            f.write(data)


def cli_misc_runpy(ctx):
    sys.argv = ['runpy'] + ctx['args']

    g = {
        'mix': Iface(),
    }

    exec(sys.stdin.read(), g, g)
