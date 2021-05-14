def package(mix):
    return {
        'build': {
            'script': mix.files.build_psh,
            'fetch': [
                {
                    'url': 'https://homebrew.bintray.com/bottles/gnu-sed-4.8.catalina.bottle.tar.gz',
                },
            ],
        },
    }
