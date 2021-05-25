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
                'boot/libcxx',
                'boot/bin/stdenv',
            ],
        },
        'runtime': {
            'depends': [
                'env/cmake',
            ],
        },
    }