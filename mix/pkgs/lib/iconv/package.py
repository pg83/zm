def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.gnu.org/pub/gnu/libiconv/libiconv-1.16.tar.gz',
                    'md5': '7d2a800b952942bb2880efb00cfd524c',
                },
            ],
            'depends': [
                'boot/make',
                'stdenv/mini',
            ],
        },
    }
