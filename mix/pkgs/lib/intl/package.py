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
                    'md5': '28b1cd4c94a74428723ed966c38cf479',
                },
            ],
            'depends': libs + [
                'tool/compress/gzip',
                'tool/gnu/findutils',
                'boot/make',
                'stdenv/mini',
            ],
        },
        'runtime': {
            'depends': libs,
        },
    }
