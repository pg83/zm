def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.gnu.org/gnu/gzip/gzip-1.10.tar.xz',
                },
            ],
            'depends': [
                'stdenv-tiny',
            ],
        },
    }
