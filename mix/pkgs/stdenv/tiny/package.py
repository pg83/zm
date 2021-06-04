def package(mix):
    return {
        'runtime': {
            'depends': [
                'tool/gnu/file',
                'tool/gnu/which',
                'tool/gnu/coreutils',
                'tool/gnu/findutils',
                'tool/text/gnu/sed',
                'tool/text/gnu/gawk',
                'tool/text/gnu/grep',
                'tool/text/gnu/patch',
                'tool/text/gnu/diffutils',
                'shell/dash/minimal',
                'stdenv/comp',
                'env/bootstrap',
            ],
        },
    }
