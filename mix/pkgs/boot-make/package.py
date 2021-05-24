def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.gnu.org/gnu/make/make-4.3.tar.gz',
                },
            ],
            'depends': [
                'bin-stdenv-tiny',
            ],
        },
    }
