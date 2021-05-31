def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.gnu.org/gnu/sed/sed-4.8.tar.xz',
                    'md5': '6d906edfdb3202304059233f51f9a71d',
                },
            ],
            'depends': [
                'boot/bin/stdenv',
            ],
        },
    }
