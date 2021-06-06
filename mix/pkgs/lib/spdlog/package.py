def package(mix):
    deps = [
        'lib/cxx',
    ]

    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://github.com/gabime/spdlog/archive/refs/tags/v1.8.5.tar.gz',
                    'md5': '8755cdbc857794730a022722a66d431a',
                },
            ],
            'depends': deps + [
                'dev/build/cmake',
                'stdenv',
            ],
        },
        'runtime': {
            'depends': deps,
        },
    }
