def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.pcre.org/pub/pcre/pcre-8.44.tar.gz',
                },
            ],
            'depends': [
                'lib/z',
                'lib/bzip2',
                'boot/pkg-config',
                'stdenv',
            ],
        },
    }
