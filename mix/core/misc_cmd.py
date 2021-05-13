import os
import sys
import subprocess


class Iface:
    def fetch_url(self, url, out):
        print('fetch ' + url + ' into ' + out)

        subprocess.check_call(['curl', '--output', out, url])


def cli_misc_runpy(ctx):
    sys.argv = ['runpy'] + ctx['args']

    g = {
        'mix': Iface(),
    }

    exec(sys.stdin.read(), g, g)
