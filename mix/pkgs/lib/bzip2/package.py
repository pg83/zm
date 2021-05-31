def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://www.sourceware.org/pub/bzip2/bzip2-latest.tar.gz',
                    'md5': '67e051268d0c475ea773822f7500d0e5',
                },
            ],
            'depends': [
                'stdenv/tiny',
            ],
        },
    }
