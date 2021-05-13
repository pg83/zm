def package(mix):
    return {
        'build': mix.files.build_sh,
        'fetch': [
            'http://mirror.keystealth.org/gnu/make/make-4.3.tar.gz',
        ],
        'depends': [
            'stdenv-boot',
        ],
    }
