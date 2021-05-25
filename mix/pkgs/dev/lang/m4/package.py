def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.gnu.org/gnu/m4/m4-1.4.18.tar.xz',
                },
                {
                    'url': 'https://raw.githubusercontent.com/macports/macports-ports/edf0ee1e2cf/devel/m4/files/secure_snprintf.patch'
                },
            ],
            'depends': [
                'lib/intl',
                'lib/sigsegv',
                'tool/build/help2man',
                'stdenv',
            ],
        },
    }
