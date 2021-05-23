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
                'glib',
                'iconv',
                'gettext',
                'slang',
                'stdenv',
                'pkg-config',
            ],
        },
    }
