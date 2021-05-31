def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.gnu.org/gnu/make/make-4.3.tar.gz',
                    'md5': 'fc7a67ea86ace13195b0bce683fd4469',
                },
            ],
            'depends': [
                'boot/bin/stdenv/tiny',
            ],
        },
    }
