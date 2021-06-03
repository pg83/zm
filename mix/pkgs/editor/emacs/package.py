def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.gnu.org/gnu/emacs/emacs-27.2.tar.xz',
                    'md5': '4c3d9ff35b2ab2fe518dc7eb3951e128',
                },
            ],
            'depends': [
                'lib/z',
                'lib/ncurses',
                'dev/build/make',
                'dev/build/pkg-config',
                'tool/compress/tar',
                'stdenv',
            ],
        },
    }
