def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.gnu.org/pub/gnu/ncurses/ncurses-6.2.tar.gz',
                    'md5': 'e812da327b1c2214ac1aed440ea3ae8d',
                },
            ],
            'depends': [
                'boot/pkg-config',
                'dev/build/make',
                'stdenv',
            ],
        },
    }
