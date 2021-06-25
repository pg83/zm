def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://pkg-config.freedesktop.org/releases/pkg-config-0.29.2.tar.gz',
                    'md5': 'f6e931e319531b736fadc017f470e68a',
                },
            ],
            'depends': [
                'boot/iconv',
                'boot/autohell',
                'boot/diffutils',
                'boot/findutils',
                'boot/coreutils',
                'boot/bin/stdenv',
            ],
        },
    }
