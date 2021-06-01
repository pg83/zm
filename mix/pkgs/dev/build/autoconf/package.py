def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.gnu.org/gnu/autoconf/autoconf-2.71.tar.xz',
                    'md5': '12cfa1687ffa2606337efe1a64416106',
                },
            ],
            'depends': [
                'dev/lang/m4',
                'dev/lang/perl5',
                'dev/build/make',
                'stdenv',
            ],
        },
        'runtime': {
            'depends': [
                'dev/lang/m4',
            ],
        },
    }
