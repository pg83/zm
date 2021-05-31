def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.gnu.org/gnu/which/which-2.21.tar.gz',
                    'md5': '097ff1a324ae02e0a3b0369f07a7544a',
                },
            ],
            'depends': [
                'boot/bin/stdenv',
            ],
        },
    }
