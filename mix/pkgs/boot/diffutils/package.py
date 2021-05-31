def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.gnu.org/gnu/diffutils/diffutils-3.7.tar.xz',
                    'md5': '4824adc0e95dbbf11dfbdfaad6a1e461',
                },
            ],
            'depends': [
                'boot/bin/stdenv',
            ],
        },
    }
