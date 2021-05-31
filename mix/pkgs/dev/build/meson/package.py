def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://github.com/mesonbuild/meson/releases/download/0.58.0/meson-0.58.0.tar.gz',
                    'md5': '18ac55e3d6a5acb17b5737eb2a15bb5b',
                },
            ],
            'depends': [
                'stdenv/tiny',
            ],
        },
        'runtime': {
            'depends': [
                'dev/lang/python3',
            ],
        },
    }
