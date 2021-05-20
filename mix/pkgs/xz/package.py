def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://tukaani.org/xz/xz-5.2.5.tar.xz',
                },
            ],
            'depends': [
                'iconv',
                'gettext',
                'stdenv-tiny',
            ],
        },
    }
