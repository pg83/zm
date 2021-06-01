def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://dist.libuv.org/dist/v1.41.0/libuv-v1.41.0.tar.gz',
                    'md5': 'd990b0770dd2b15f7a8399580d55d32c',
                },
            ],
            'depends': [
                'dev/build/autoconf',
                'dev/build/automake',
                'dev/build/libtool',
                'dev/build/make',
                'stdenv',
            ],
        },
    }
