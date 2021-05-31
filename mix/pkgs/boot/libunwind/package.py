def package(mix):
    url = 'https://github.com/llvm/llvm-project/releases/download/llvmorg-12.0.0/libunwind-12.0.0.src.tar.xz'

    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': url,
                    'md5': 'a41e903c1989df7de8c39b65fc43467b',
                },
            ],
            'depends': [
                'boot/bin/stdenv',
            ],
        },
    }
