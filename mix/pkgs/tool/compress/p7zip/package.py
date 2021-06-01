def package(mix):
    url = 'https://downloads.sourceforge.net/project/p7zip/p7zip/16.02/p7zip_16.02_src_all.tar.bz2'

    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': url,
                    'md5': '',
                },
            ],
            'depends': [
                'lib/cxx',
                'dev/build/make',
                'stdenv',
            ],
        },
    }
