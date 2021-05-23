def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://github.com/mesonbuild/meson/releases/download/0.58.0/meson-0.58.0.tar.gz',
                },
            ],
            'depends': [
                'stdenv-tiny',
            ],
        },
        'runtime': {
            'depends': [
                'python',
            ],
        },
    }
