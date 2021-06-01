def package(mix):
    url = 'https://raw.githubusercontent.com/macports/macports-ports/edf0ee1e2cf/devel/m4/files/secure_snprintf.patch'

    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.gnu.org/gnu/m4/m4-1.4.18.tar.xz',
                    'md5': '730bb15d96fffe47e148d1e09235af82',
                },
                {
                    'url': url,
                    'md5': '319c143996239e23d2fe3e7968a7620d',
                },
            ],
            'depends': [
                'lib/intl',
                'lib/sigsegv',
                'dev/build/make',
                'dev/build/help2man',
                'stdenv',
            ],
        },
    }
