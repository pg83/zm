def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.pcre.org/pub/pcre/pcre2-10.36.tar.gz',
                    'md5': 'a5d9aa7d18b61b0226696510e60c9582',
                },
            ],
            'depends': [
                'lib/z',
                'lib/bzip2',
                'dev/build/make',
                'boot/pkg-config',
                'stdenv',
            ],
        },
    }
