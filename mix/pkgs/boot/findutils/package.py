def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.gnu.org/gnu/findutils/findutils-4.8.0.tar.xz',
                    'md5': 'eeefe2e6380931a77dfa6d9350b43186',
                },
            ],
            'depends': [
                'boot/autohell',
                'boot/coreutils',
                'boot/bin/stdenv',
            ],
        },
    }
