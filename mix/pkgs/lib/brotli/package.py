def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://github.com/google/brotli/archive/refs/tags/v1.0.9.tar.gz',
                    'md5': 'c2274f0c7af8470ad514637c35bcee7d',
                },
            ],
            'depends': [
                'dev/build/make',
                'stdenv/tiny',
            ],
        },
    }
