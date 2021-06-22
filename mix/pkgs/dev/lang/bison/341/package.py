def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.gnu.org/gnu/bison/bison-3.4.1.tar.xz',
                    'md5': '201286a573b12da109df96282fe4ff4a',
                },
                {
                    'url': 'https://storage.yandexcloud.net/mix-cache/bison-bootstrap-master.tar.bz2',
                    'md5': '425bbc1c4a21e708f05d35c62210f5ee',
                },
            ],
            'depends': [
                'lib/intl',
                'dev/lang/m4',
                'dev/lang/perl5',
                'dev/build/make',
                'stdenv',
            ],
        },
    }
