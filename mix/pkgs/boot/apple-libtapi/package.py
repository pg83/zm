def package(mix):
    url = 'https://github.com/tpoechtrager/apple-libtapi/archive/664b8414f89612f2dfd35a9b679c345aa5389026.zip'

    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': url,
                },
            ],
            'depends': [
                'boot/cmake',
                'boot/which',
                'boot/libcxx',
                'boot/diffutils',
                'boot/bin/stdenv',
            ],
        },
    }
