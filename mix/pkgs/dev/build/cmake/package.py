def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://github.com/Kitware/CMake/releases/download/v3.20.2/cmake-3.20.2.tar.gz',
                    'md5': 'cd0e7735f1e51f30ee3b0844390a464a',
                },
            ],
            'depends': [
                'lib/z',
                'lib/xz',
                'lib/uv',
                'lib/cxx',
                'lib/curl',
                'lib/bzip2',
                'lib/expat',
                'lib/archive',
                'dev/build/ninja',
                'boot/cmake',
                'boot/pkg-config',
                'stdenv',
            ],
        },
        'runtime': {
            'depends': [
                'env/cmake',
            ],
        },
    }
