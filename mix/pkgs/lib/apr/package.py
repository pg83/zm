def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://archive.apache.org/dist/apr/apr-1.7.0.tar.bz2',
                    'md5': '7a14a83d664e87599ea25ff4432e48a7',
                },
            ],
            'depends': [
                'dev/build/make',
                'dev/build/pkg-config',
                'stdenv',
            ],
        },
    }
