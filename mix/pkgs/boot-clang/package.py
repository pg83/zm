def package(mix):
    url = 'https://github.com/llvm/llvm-project/releases/download/llvmorg-12.0.0/llvm-project-12.0.0.src.tar.xz'

    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': url,
                },
            ],
            'depends': [
                'boot-which',
                'boot-libcxx',
                'boot-cmake',
                'boot-python',
                'boot-ninja',
                'bin-stdenv',
            ],
        },
        'runtime': {
            'depends': [
                'env-system',
            ],
        },
    }
