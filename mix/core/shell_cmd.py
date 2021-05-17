import subprocess


def unzip(path):
    print('unzip ' + path)

    import zipfile

    with zipfile.ZipFile(path, 'r') as f:
        f.extractall()


def untar(path):
    print('untar ' + path)

    try:
        return untar_tar(path)
    except FileNotFoundError:
        pass

    return untar_tarfile(path)


def untar_tar(path):
    subprocess.check_call(['tar', '-xf', path])


def untar_tarfile(path):
    import tarfile

    with tarfile.open(path) as f:
        f.extractall()


def fetch_url(url, out):
    print('fetch ' + url + ' into ' + out)

    try:
        return fetch_curl(url, out)
    except FileNotFoundError:
        pass

    return fetch_urllib(url, out)


def fetch_curl(url, out):
    subprocess.check_call(['curl', '--output', out, url])


def fetch_urllib(url, out):
    import ssl
    import urllib.request as ur

    ssl._create_default_https_context = ssl._create_unverified_context

    def iter_chunks():
        r = ur.urlopen(url)

        while True:
            c = r.read(1 * 1024 * 1024)

            if c:
                yield c
            else:
                return

    with open(out, 'wb') as f:
        cnt = 0

        for c in iter_chunks():
            cnt += len(c)

            print('got ' + str(cnt) + ' bytes')

            f.write(c)
