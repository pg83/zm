def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.gnu.org/gnu/diffutils/diffutils-3.7.tar.xz',
                },
            ],
            'depends': [
                'boot/bin/stdenv',
            ],
        },
    }
