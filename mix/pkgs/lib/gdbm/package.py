def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.gnu.org/gnu/gdbm/gdbm-1.19.tar.gz',
                },
            ],
            'depends': [
                'lib/intl',
                'lib/iconv',
                'lib/readline',
                'stdenv',
            ],
        },
    }
