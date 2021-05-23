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
                'python',
                'libcxx',
                'stdenv',
            ],
        },
    }
