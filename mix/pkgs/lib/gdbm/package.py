def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.gnu.org/gnu/gdbm/gdbm-1.19.tar.gz',
                    'md5': 'aeb29c6a90350a4c959cd1df38cd0a7e',
                },
            ],
            'depends': [
                'lib/intl',
                'lib/iconv',
                'lib/readline',
                'dev/build/make',
                'stdenv',
            ],
        },
    }
