def package(mix):
    return {
        'build': {
            'script': mix.files.build_ph,
            'fetch': [
                {
                    'url': 'https://homebrew.bintray.com/bottles/dash-0.5.11.3.catalina.bottle.tar.gz',
                    'md5': '7c1b205c147038bfc901c9c27dd7cd03',
                },
            ],
        },
    }
