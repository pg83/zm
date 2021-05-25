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
                },
            ],
            'depends': [
                'boot/bin/stdenv',
            ] + deps,
        },
        'runtime': {
            'depends': deps,
        },
    }
