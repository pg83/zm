def package(mix):
    up = 'https://raw.githubusercontent.com/Homebrew/patches/'

    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://ftp.openbsd.org/pub/OpenBSD/OpenSSH/portable/openssh-8.6p1.tar.gz',
                    'md5': '805f7048aec6dd752584e570383a6f00',
                },
                {
                    'url': up + '1860b0a745f1fe726900974845d1b0dd3c3398d6/openssh/patch-sandbox-darwin.c-apple-sandbox-named-external.diff',
                    'md5': '33cc7e83ce4fe6ecadd1283967f795c3',
                },
                {
                    'url': up + 'd8b2d8c2612fd251ac6de17bf0cc5174c3aab94c/openssh/patch-sshd.c-apple-sandbox-named-external.diff',
                    'md5': 'a50fb1d7c40ac7fac3360218cb37a38b',
                },
            ],
            'depends': [
                'lib/z',
                'lib/edit',
                'lib/ldns',
                'lib/openssl',
                'dev/build/make',
                'dev/build/pkg-config',
                'tool/text/gnu/patch',
                'stdenv',
            ],
        },
    }
