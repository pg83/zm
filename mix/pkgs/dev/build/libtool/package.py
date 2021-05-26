def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftpmirror.gnu.org/libtool/libtool-2.4.6.tar.gz',
                },
            ],
            'depends': [
                'dev/lang/m4',
                'stdenv',
            ],
        },
    }
