def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://github.com/ninja-build/ninja/archive/refs/tags/v1.10.2.tar.gz',
                    'md5': '639f75bc2e3b19ab893eaf2c810d4eb4',
                },
            ],
            'depends': [
                'boot/sed',
                'boot/python',
                'boot/libcxx',
                'boot/coreutils',
                'boot/bin/stdenv',
            ],
        },
    }
