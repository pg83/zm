def package(mix):
    url = 'https://github.com/tpoechtrager/apple-libtapi/archive/664b8414f89612f2dfd35a9b679c345aa5389026.zip'

    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': url,
                    'md5': '30c0321c2099e3eac31110e5aaf56fbe',
                },
            ],
            'depends': [
                'boot/ninja',
                'boot/cmake',
                'boot/which',
                'boot/python',
                'boot/libcxx',
                'boot/autohell',
                'boot/diffutils',
                'boot/coreutils',
                'boot/bin/stdenv',
                'env/compiler',
                'env/cmake',
            ],
        },
    }
