def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'http://ftp.midnight-commander.org/mc-4.8.26.tar.xz',
                    'md5': '3c1f77b71dba1f4eeeedc4276627fed7',
                },
            ],
            'depends': [
                'lib/intl',
                'lib/glib',
                'lib/iconv',
                'lib/ncurses',
                'dev/build/make',
                'dev/build/pkg-config',
                'stdenv',
            ],
        },
    }
