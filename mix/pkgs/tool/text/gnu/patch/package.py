def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.gnu.org/gnu/patch/patch-2.7.6.tar.xz',
                    'md5': '78ad9937e4caadcba1526ef1853730d5',
                },
            ],
            'depends': [
                'lib/intl',
                'lib/iconv',
                'dev/build/make',
                'stdenv/c',
                'boot/stdenv',
            ],
        },
    }
