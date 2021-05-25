def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.gnu.org/gnu/findutils/findutils-4.8.0.tar.xz',
                },
            ],
            'depends': [
                'lib/iconv',
                'dev/lang/clang',
                'boot/stdenv',
            ],
        },
    }
