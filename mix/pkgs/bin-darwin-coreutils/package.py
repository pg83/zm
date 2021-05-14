def package(mix):
    return {
        'build': {
            'script': mix.files.build_ph,
            'fetch': [
                {
                    'url': 'https://homebrew.bintray.com/bottles/coreutils-8.32.catalina.bottle.tar.gz',
                },
            ],
        },
    }
