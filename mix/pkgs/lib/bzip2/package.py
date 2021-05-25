def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://www.sourceware.org/pub/bzip2/bzip2-latest.tar.gz',
                },
            ],
            'depends': [
                'stdenv/tiny',
            ],
        },
    }
