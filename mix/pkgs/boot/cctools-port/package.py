def package(mix):
    url = 'https://github.com/tpoechtrager/cctools-port/archive/236a426c1205a3bfcf0dbb2e2faf2296f0a100e5.zip'

    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': url,
                },
            ],
            'depends': [
                'boot/libcxx',
                'boot/diffutils',
                'boot/bin/stdenv',
            ],
        },
    }
