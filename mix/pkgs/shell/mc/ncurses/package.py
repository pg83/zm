def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'http://ftp.midnight-commander.org/mc-4.8.26.tar.xz',
                },
            ],
            'depends': [
                'lib/intl',
                'lib/glib',
                'lib/iconv',
                'lib/ncurses',
                'tool/build/pkg-config',
                'stdenv',
            ],
        },
    }
