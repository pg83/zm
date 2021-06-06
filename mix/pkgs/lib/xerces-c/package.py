def package(mix):
    deps = [
        'lib/cxx',
        'lib/curl',
        'lib/iconv',
    ]

    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://archive.apache.org/dist/xerces/c/3/sources/xerces-c-3.2.3.tar.gz',
                    'md5': 'a5fa4d920fce31c9ca3bfef241644494',
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
