def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://github.com/JuliaStrings/utf8proc/archive/v2.6.1.tar.gz',
                    'md5': '9fe61625c105f911a2c89423f071ef1d',
                },
            ],
            'depends': [
                'dev/build/make',
                'stdenv',
            ],
        },
    }
