def package(mix):
    url = 'https://src.fedoraproject.org/repo/pkgs/zip/zip30.tar.gz/7b74551e63f8ee6aab6fbc86676c0d37/zip30.tar.gz'

    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': url,
                },
            ],
            'depends': [
                'stdenv',
            ],
        },
    }
