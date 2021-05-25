def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'http://deb.debian.org/debian/pool/main/f/file/file_5.39.orig.tar.gz',
                },
            ],
            'depends': [
                'boot/stdenv',
            ],
        },
    }
