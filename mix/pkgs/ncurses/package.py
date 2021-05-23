def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.gnu.org/pub/gnu/ncurses/ncurses-6.2.tar.gz',
                },
            ],
            'depends': [
                'stdenv',
                'boot-pkg-config',
            ],
        },
    }
