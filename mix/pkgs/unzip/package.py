def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://downloads.sourceforge.net/project/infozip/UnZip%206.x%20%28latest%29/UnZip%206.0/unzip60.tar.gz',
                },
                {
                    'url': 'https://deb.debian.org/debian/pool/main/u/unzip/unzip_6.0-26.debian.tar.xz',
                },
            ],
            'depends': [
                'patch',
                'stdenv-tiny',
            ],
        },
    }
