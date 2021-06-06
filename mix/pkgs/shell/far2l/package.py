def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://github.com/pg83/far2l/archive/0ff21b859c9a3ffeb1b9fd541dd03f9b398b0b3a.zip',
                    'md5': 'fbb070521047b8589615b490686b6f8c',
                },
            ],
            'depends': [
                'lib/ssh',
                'lib/pcre',
                'lib/spdlog',
                'lib/archive',
                'lib/xerces-c',
                'lib/uchardet',
                'dev/build/pkg-config',
                'dev/build/cmake',
                'dev/lang/m4',
                'stdenv',
            ],
        },
    }
