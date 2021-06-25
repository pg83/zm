def package(mix):
    return {
        'build': {
            'script': mix.files.build_py,
            'fetch': [
                {
                    'url': 'https://github.com/pg83/heirloom/archive/7d0ef303ebab2fee61dc894caf6f3bfde564b7be.zip',
                    'md5': 'ca952ec8bd49691d0be22f9e013fd053',
                },
            ],
            'depends': [
                'boot/bin/stdenv',
            ],
        },
    }
