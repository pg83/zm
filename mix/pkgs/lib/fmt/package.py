def package(mix):
    deps = [
        'lib/cxx',
    ]

    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://github.com/fmtlib/fmt/archive/refs/tags/7.1.3.tar.gz',
                    'md5': '2522ec65070c0bda0ca288677ded2831',
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
