def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://invisible-mirror.net/archives/mawk/mawk-1.3.4-20200120.tgz',
                    'md5': 'd48752f402d7371d9eb5f68de3da05d4',
                },
            ],
            'depends': [
                'lib/readline',
                'dev/build/make',
                'stdenv',
            ],
        },
    }
