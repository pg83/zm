def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://github.com/magiblot/turbo/archive/971aad35d4b705228caa8852114438ee71d488d8.zip',
                    'md5': '53d2cdb6a47cad1796d32dc5839726e8',
                },
            ],
            'depends': [
                'lib/cxx',
                'lib/fmt',
                'lib/tvision',
                'lib/clipboard',
                'dev/build/cmake',
                'stdenv',
            ],
        },
    }
