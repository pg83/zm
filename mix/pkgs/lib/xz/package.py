def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://tukaani.org/xz/xz-5.2.5.tar.xz',
                    'md5': 'aa1621ec7013a19abab52a8aff04fe5b',
                },
            ],
            'depends': [
                'lib/intl',
                'lib/iconv',
                'stdenv/tiny',
            ],
        },
    }
