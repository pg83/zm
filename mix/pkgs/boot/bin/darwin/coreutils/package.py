def package(mix):
    return {
        'build': {
            'script': mix.files.build_ph,
            'fetch': [
                {
                    'url': 'https://homebrew.bintray.com/bottles/coreutils-8.32.catalina.bottle.tar.gz',
                    'md5': 'ae4a54ed36421e1a2909e88b006a5d01',
                },
            ],
        },
    }
