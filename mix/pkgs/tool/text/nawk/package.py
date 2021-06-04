def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://github.com/onetrueawk/awk/archive/c0f4e97e4561ff42544e92512bbaf3d7d1f6a671.zip',
                    'md5': '8fd8db2c605c68fc1d90391b95336e3b',
                },
            ],
            'depends': [
                'dev/lang/bison',
                'dev/build/make',
                'stdenv',
            ],
        },
    }
