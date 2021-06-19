def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://github.com/thepowersgang/mrustc/archive/78742ef9de9e162373b46ac179bc2724d45a3cd7.zip',
                    'md5': 'a7020e5434609495269611e2abcb95d1',
                },
            ],
            'depends': [
                'lib/z',
                'lib/cxx',
                'lib/curl',
                'shell/bash',
                'dev/vcs/git',
                'tool/gnu/tar',
                'dev/build/make',
                'dev/build/cmake',
                'env/compiler',
                'stdenv',
            ],
        },
    }
