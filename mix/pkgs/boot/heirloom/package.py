def package(mix):
    return {
        'build': {
            'script': mix.files.build_py,
            'fetch': [
                {
                    'url': 'https://github.com/pg83/heirloom/archive/c36382e29f4578ebe43ea398fa0f6f654b1d7fb7.zip',
                    'md5': '1b302a8842925412a079ea5123a95ebe',
                },
            ],
            'depends': [
                'boot/bin/stdenv',
            ],
        },
    }
