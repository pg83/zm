def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftpmirror.gnu.org/libtool/libtool-2.4.6.tar.gz',
                    'md5': 'addf44b646ddb4e3919805aa88fa7c5e',
                },
            ],
            'depends': [
                'dev/lang/m4',
                'dev/build/make',
                'stdenv',
            ],
        },
    }
