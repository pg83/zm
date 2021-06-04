def package(mix):
    deps = [
        'lib/z',
        'lib/apr',
        'lib/openssl',
        'lib/apr-util',
    ]

    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://www.apache.org/dist/serf/serf-1.3.9.tar.bz2',
                    'md5': '370a6340ff20366ab088012cd13f2b57',
                },
            ],
            'depends': deps + [
                'dev/build/scons',
                'tool/text/gnu/patch',
                'stdenv',
            ],
        },
    }
