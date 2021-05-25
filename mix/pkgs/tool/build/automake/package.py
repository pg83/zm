def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.gnu.org/gnu/automake/automake-1.16.3.tar.xz',
                },
            ],
            'depends': [
                'dev/lang/perl5',
                'tool/build/autoconf',
                'stdenv',
            ],
        },
    }
