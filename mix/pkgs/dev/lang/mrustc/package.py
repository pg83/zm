def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://github.com/thepowersgang/mrustc/archive/78742ef9de9e162373b46ac179bc2724d45a3cd7.zip',
                    'md5': 'a7020e5434609495269611e2abcb95d1',
                },
                {
                    'url': 'https://static.rust-lang.org/dist/rustc-1.29.0-src.tar.gz',
                    'md5': '54c3f0ffb826bdcc2a7395468828a94c',
                },
            ],
            'depends': [
                'lib/z',
                'lib/cxx',
                'lib/curl',
                'lib/iconv',
                'lib/openssl',
                'tool/curl',
                'shell/bash',
                'dev/vcs/git',
                'tool/gnu/tar',
                'tool/gnu/time',
                'dev/lang/python3',
                'dev/build/make',
                'dev/build/cmake',
                'env/compiler',
                'stdenv',
            ],
        },
    }
