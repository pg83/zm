def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.gnu.org/gnu/sed/sed-4.8.tar.xz',
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
