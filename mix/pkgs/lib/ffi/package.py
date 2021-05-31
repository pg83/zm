def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://sourceware.org/ftp/libffi/libffi-3.3.tar.gz',
                    'md5': '6313289e32f1d38a9df4770b014a2ca7',
                },
            ],
            'depends': [
                'tool/gnu/sed',
                'stdenv/tiny',
            ],
        },
    }
