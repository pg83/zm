def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://www.bytereef.org/software/mpdecimal/releases/mpdecimal-2.5.1.tar.gz',
                    'md5': '18599e4ffcfe8cd93e0efa8f14f027eb',
                },
            ],
            'depends': [
                'stdenv',
            ],
        },
    }
