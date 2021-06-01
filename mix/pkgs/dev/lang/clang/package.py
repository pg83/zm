def package(mix):
    url = 'https://github.com/llvm/llvm-project/releases/download/llvmorg-12.0.0/llvm-project-12.0.0.src.tar.xz'

    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': url,
                    'md5': '5a4fab4d7fc84aefffb118ac2c8a4fc0',
                },
            ],
            'depends': [
                'boot/ninja',
                'boot/cmake',
                'boot/stdenv',
            ],
        },
        'runtime': {
            'depends': [
                'dev/lang/cctools',
                'env/system',
            ],
        },
    }
