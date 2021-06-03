def package(mix):
    url = 'https://files.pythonhosted.org/packages/be/d0/bf4e7003369c6d8a6e490741c54791c7918d9ef10b56aec201e76706f1d7/SCons-4.1.0.post1.tar.gz'

    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': url,
                    'md5': '2b1daf6c83e467ae41c742f546c2fe5a',
                },
            ],
            'depends': [
                'stdenv',
            ],
        },
        'runtime': {
            'depends': [
                'dev/lang/python3',
            ],
        },
    }
