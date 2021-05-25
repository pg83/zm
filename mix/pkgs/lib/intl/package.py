def package(mix):
    libs = [
        'lib/iconv',
        'lib/unistring',
    ]

    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.gnu.org/pub/gnu/gettext/gettext-0.21.tar.gz',
                },
            ],
            'depends': libs + [
                'tool/compress/gzip',
                'dev/lang/clang',
                'tool/gnu/findutils',
                'boot/stdenv',
            ],
        },
        'runtime': {
            'depends': libs,
        },
    }
