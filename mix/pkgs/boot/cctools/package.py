def package(mix):
    url = 'https://github.com/tpoechtrager/cctools-port/archive/236a426c1205a3bfcf0dbb2e2faf2296f0a100e5.zip'

    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': url,
                    'md5': '3ba3b9f5e6ebc2afe77cdafeaaeeb981',
                },
            ],
            'depends': [
                'boot/libcxx',
                'boot/cctools/libtapi',
                'boot/autohell',
                'boot/diffutils',
                'boot/coreutils',
                'boot/bin/stdenv',
            ],
        },
    }
