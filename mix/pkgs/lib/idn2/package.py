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
                },
            ],
            'depends': libs + [
                'tool/build/pkg-config',
                'stdenv',
            ],
        },
        'runtime': {
            'depends': libs,
        },
    }
