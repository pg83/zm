def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.gnu.org/gnu/patch/patch-2.7.6.tar.xz',
                },
            ],
            'depends': [
                'lib/intl',
                'lib/iconv',
                'dev/lang/clang',
                'boot/stdenv',
            ],
        },
    }
