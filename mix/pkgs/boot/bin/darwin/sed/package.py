def package(mix):
    return {
        'build': {
            'script': mix.files.build_ph,
            'fetch': [
                {
                    'url': 'https://homebrew.bintray.com/bottles/gnu-sed-4.8.catalina.bottle.tar.gz',
                    'md5': '753ed1c9c1225ca7c4d47b15ee8d5a3f',
                },
            ],
        },
    }
