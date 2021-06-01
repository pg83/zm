def package(mix):
    libs = [
        'lib/intl',
        'lib/iconv',
        'lib/unistring',
    ]

    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.gnu.org/gnu/libidn/libidn2-2.3.1.tar.gz',
                    'md5': 'cda07f5ac55fccfafdf7ee01828adad5',
                },
            ],
            'depends': libs + [
                'dev/build/make',
                'dev/build/pkg-config',
                'stdenv',
            ],
        },
        'runtime': {
            'depends': libs,
        },
    }
