def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://github.com/libexpat/libexpat/releases/download/R_2_4_1/expat-2.4.1.tar.xz',
                    'md5': 'a4fb91a9441bcaec576d4c4a56fa3aa6',
                },
            ],
            'depends': [
                'stdenv',
            ],
        },
    }
