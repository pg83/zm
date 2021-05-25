def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'http://gondor.apana.org.au/~herbert/dash/files/dash-0.5.11.3.tar.gz',
                },
            ],
            'depends': [
                'lib/intl',
                'lib/iconv',
                'dev/lang/clang',
                'boot/stdenv',
            ],
        },
    }
