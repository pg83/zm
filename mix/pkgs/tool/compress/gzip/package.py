def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.gnu.org/gnu/gzip/gzip-1.10.tar.xz',
                    'md5': '691b1221694c3394f1c537df4eee39d3',
                },
            ],
            'depends': [
                'boot/make',
                'boot/stdenv',
            ],
        },
    }
