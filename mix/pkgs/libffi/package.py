def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://sourceware.org/ftp/libffi/libffi-3.3.tar.gz',
                },
            ],
            'depends': [
                'sed',
                'stdenv-tiny',
            ],
        },
    }
