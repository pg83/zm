def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.gnu.org/gnu/libsigsegv/libsigsegv-2.13.tar.gz',
                    'md5': 'cf4a5fdc95e5494eaa190825af11f3be',
                },
            ],
            'depends': [
                'dev/build/make',
                'stdenv/mini',
            ],
        },
    }
