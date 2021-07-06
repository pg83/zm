def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.gnu.org/gnu/coreutils/coreutils-8.32.tar.xz',
                    'md5': '022042695b7d5bcf1a93559a9735e668',
                },
            ],
            'depends': [
                'stdenv/c',
                'lib/intl',
                'lib/iconv',
                'lib/sigsegv',
                'dev/build/make',
                'boot/stdenv',
            ],
        },
    }
