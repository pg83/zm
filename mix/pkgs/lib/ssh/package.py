def package(mix):
    deps = [
        'lib/z',
        'lib/cxx',
        'lib/openssl',
    ]

    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://www.libssh.org/files/0.9/libssh-0.9.5.tar.xz',
                    'md5': '6211e47ba4dfd7f7e9f8a17a601245f4',
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
