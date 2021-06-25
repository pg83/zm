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
                'boot/which',
                'boot/cmake',
                'boot/ninja',
                'boot/python',
                'boot/libcxx',
                'boot/autohell',
                'boot/coreutils',
                'boot/bin/stdenv',
            ],
        },
        'runtime': {
            'depends': [
                'boot/cctools',
                'env/system',
            ],
        },
    }
