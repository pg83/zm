def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://archive.apache.org/dist/subversion/subversion-1.14.1.tar.bz2',
                    'md5': '2eccc2c7451397e01a13682600af9563',
                },
            ],
            'depends': [
                'lib/z',
                'lib/lz4',
                'lib/apr',
                'lib/intl',
                'lib/serf',
                'lib/expat',
                'lib/sqlite3',
                'lib/apr-util',
                'lib/utf8proc',
                'dev/build/make',
                'dev/build/pkg-config',
                'stdenv',
            ],
        },
    }
