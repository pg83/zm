def package(mix):
    deps = [
        'boot/libcxxrt',
    ]

    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://github.com/llvm/llvm-project/releases/download/llvmorg-12.0.0/libcxx-12.0.0.src.tar.xz',
                },
            ],
            'depends': [
                'boot/bin/stdenv',
            ] + deps,
        },
        'runtime': {
            'depends': deps,
        },
    }