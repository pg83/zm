def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.gnu.org/gnu/automake/automake-1.16.3.tar.xz',
                    'md5': 'c27f608a4e1f302ec7ce42f1251c184e',
                },
            ],
            'depends': [
                'dev/lang/perl5',
                'dev/build/autoconf',
                'dev/build/make',
                'stdenv',
            ],
        },
    }
