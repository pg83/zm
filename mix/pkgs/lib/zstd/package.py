def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://github.com/facebook/zstd/releases/download/v1.5.0/zstd-1.5.0.tar.gz',
                    'md5': 'a6eb7fb1f2c21fa80030a47993853e92',
                },
            ],
            'depends': [
                'dev/build/make',
                'stdenv/tiny',
            ],
        },
    }
