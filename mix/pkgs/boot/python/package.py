def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://www.python.org/ftp/python/3.9.5/Python-3.9.5.tar.xz',
                    'md5': '71f7ada6bec9cdbf4538adc326120cfd',
                },
            ],
            'depends': [
                'boot/bin/stdenv',
            ],
        },
    }
