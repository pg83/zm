def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://github.com/ninja-build/ninja/archive/refs/tags/v1.10.2.tar.gz',
                },
            ],
            'depends': [
                'lib/cxx',
                'dev/lang/python3',
                'stdenv',
            ],
        },
    }
