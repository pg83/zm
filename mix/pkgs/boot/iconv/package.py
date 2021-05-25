def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.gnu.org/pub/gnu/libiconv/libiconv-1.16.tar.gz',
                },
            ],
            'depends': [
                'boot/bin/stdenv',
            ],
        },
    }
