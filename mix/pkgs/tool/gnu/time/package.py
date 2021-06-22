def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.gnu.org/gnu/time/time-1.9.tar.gz',
                    'md5': 'd2356e0fe1c0b85285d83c6b2ad51b5f',
                },
            ],
            'depends': [
                'dev/build/make',
                'stdenv',
            ],
        },
    }
