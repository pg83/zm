def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://www.python.org/ftp/python/3.9.5/Python-3.9.5.tar.xz',
                },
            ],
            'depends': [
                'boot/bin/stdenv',
            ],
        },
    }
