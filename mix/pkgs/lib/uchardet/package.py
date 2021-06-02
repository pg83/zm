def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://github.com/freedesktop/uchardet/archive/refs/tags/v0.0.7.tar.gz',
                    'md5': 'f1ac05da2edfc17b12d1f942695f59b8',
                },
            ],
            'depends': [
                'lib/cxx',
                'dev/build/ninja',
                'dev/build/cmake',
                'stdenv',
            ],
        },
    }
