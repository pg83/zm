def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://github.com/Kitware/CMake/releases/download/v3.20.2/cmake-3.20.2.tar.gz',
                },
            ],
            'depends': [
                'lib/z',
                'lib/xz',
                'lib/cxx',
                'lib/bzip2',
                'lib/expat',
                'lib/archive',
                'tool/build/ninja',
                'boot/cmake',
                'stdenv',
            ],
        },
        'runtime': {
            'depends': [
                'env/cmake',
            ],
        },
    }
