def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.gnu.org/gnu/grep/grep-3.6.tar.xz',
                    'md5': 'f47fe27049510b2249dba7f862ac1b51',
                },
            ],
            'depends': [
                'lib/intl',
                'lib/iconv',
                'dev/build/make',
                'stdenv/mini',
            ],
        },
    }
