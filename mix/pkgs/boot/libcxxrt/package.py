def package(mix):
    deps = [
        'boot/libunwind',
    ]

    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://github.com/libcxxrt/libcxxrt/archive/refs/heads/master.zip',
                    'md5': '3b43179e518dd0a54362267b255b9d24',
                },
            ],
            'depends': deps + [
                'boot/coreutils',
                'boot/bin/stdenv',
            ],
        },
        'runtime': {
            'depends': deps,
        },
    }
