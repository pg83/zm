def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://github.com/jtanx/libclipboard/archive/refs/tags/v1.1.tar.gz',
                    'md5': 'bddc22070b6804ed63994af49b778b70',
                },
            ],
            'depends': [
                'dev/build/cmake',
                'dev/build/pkg-config',
                'stdenv',
            ],
        },
    }
