def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://mirror.tochlab.net/pub/gnu/gawk/gawk-5.1.0.tar.xz',
                    'md5': '8470c34eeecc41c1aa0c5d89e630df50',
                },
            ],
            'depends': [
                'lib/intl',
                'lib/iconv',
                'lib/sigsegv',
                'dev/build/make',
                'stdenv/c',
                'boot/stdenv',
            ],
        },
    }
