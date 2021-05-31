def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.gnu.org/gnu/termcap/termcap-1.3.1.tar.gz',
                    'md5': 'ffe6f86e63a3a29fa53ac645faaabdfa',
                },
            ],
            'depends': [
                'stdenv',
            ],
        },
    }
