def package(mix):
    url = 'https://downloads.sourceforge.net/project/infozip/UnZip%206.x%20%28latest%29/UnZip%206.0/unzip60.tar.gz'

    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': url,
                    'md5': '62b490407489521db863b523a7f86375',
                },
                {
                    'url': 'https://deb.debian.org/debian/pool/main/u/unzip/unzip_6.0-26.debian.tar.xz',
                    'md5': 'e2bf7537e1ca821f6059ee84e7ae76a5',
                },
            ],
            'depends': [
                'dev/build/make',
                'tool/text/gnu/patch',
                'stdenv/tiny',
                'stdenv/c',
            ],
        },
    }
