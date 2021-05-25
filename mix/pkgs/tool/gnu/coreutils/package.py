def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.gnu.org/gnu/coreutils/coreutils-8.32.tar.xz',
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