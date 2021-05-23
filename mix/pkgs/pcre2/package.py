def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.pcre.org/pub/pcre/pcre2-10.36.tar.gz',
                },
            ],
            'depends': [
                'stdenv',
                'zlib',
                'bzip2',
                'boot-pkg-config',
            ],
        },
    }
