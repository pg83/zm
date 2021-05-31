def package(mix):
    url = 'https://github.com/llvm/llvm-project/releases/download/llvmorg-12.0.0/clang+llvm-12.0.0-x86_64-apple-darwin.tar.xz'

    return {
        'build': {
            'script': mix.files.build_ph,
            'fetch': [
                {
                    'url': url,
                    'md5': '7bac46e8c20b3b227efc9e65dbddcea1',
                },
            ],
        },
    }
