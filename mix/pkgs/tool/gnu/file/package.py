def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'http://deb.debian.org/debian/pool/main/f/file/file_5.39.orig.tar.gz',
                    'md5': '1c450306053622803a25647d88f80f25',
                },
            ],
            'depends': [
                'boot/stdenv',
            ],
        },
    }
