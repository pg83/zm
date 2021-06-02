def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://github.com/elfmz/far2l/archive/refs/tags/v2021-04-26_alpha.tar.gz',
                    'md5': '508477c54a5fb7e2cde798c65d45fca8',
                },
            ],
            'depends': [
                'lib/ssh',
                'lib/pcre2',
                'lib/spdlog',
                'lib/archive',
                'lib/xerces-c',
                'lib/uchardet',
                'dev/build/ninja',
                'dev/build/pkg-config',
                'dev/build/cmake',
                'dev/lang/m4',
                'stdenv',
            ],
        },
    }
