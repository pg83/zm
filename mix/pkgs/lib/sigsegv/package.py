def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.gnu.org/gnu/libsigsegv/libsigsegv-2.13.tar.gz',
                },
            ],
            'depends': [
                'stdenv',
            ],
        },
    }
