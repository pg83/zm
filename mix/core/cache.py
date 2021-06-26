import os
import hashlib
import subprocess

import core.manager as cm
import core.shell_cmd as cs


def aws_cmd(*args):
    url = 'https://storage.yandexcloud.net'

    return ['aws', '--endpoint-url=' + url, 's3'] + [x for x in args]


def list_cache():
    for l in subprocess.check_output(aws_cmd('ls', 's3://mix-cache/cache/')).decode().split('\n'):
        if l.strip():
            el = os.path.basename(l.split(' ')[-1])

            if el:
                yield el


def store_cache(path):
    subprocess.check_call(aws_cmd('cp', path, 's3://mix-cache/cache/' + os.path.basename(path)))


def cli_cache(ctx):
    args = ctx['args']
    binary = ctx['binary']
    where = os.path.join(os.path.dirname(binary), 'pkgs')

    def iter_urls():
        for p in cm.Manager(binary, where).all_packages():
            yield from p.urls

    in_cache = set(list_cache())

    for el in iter_urls():
        print(f'process {el}')

        if 'md5' not in el:
            print(f'no md5 in {el}, skip')

            continue

        md5 = el['md5']

        if md5 in in_cache:
            continue

        url = el['url']

        try:
            cs.fetch_url(url, md5)

            if hashlib.md5(open(md5, 'rb').read()).hexdigest() != md5:
                print(f'incorrect md5 in {el}, skip')

                continue

            store_cache(md5)
        finally:
            os.unlink(md5)

        in_cache.add(md5)
