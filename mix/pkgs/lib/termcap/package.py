def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.gnu.org/gnu/termcap/termcap-1.3.1.tar.gz',
                },
            ],
            'depends': [
                'stdenv',
            ],
        },
    }
