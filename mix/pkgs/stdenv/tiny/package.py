def package(mix):
    return {
        'runtime': {
            'depends': [
                'tool/gnu/sed',
                'tool/gnu/file',
                'tool/gnu/gawk',
                'tool/gnu/grep',
                'tool/gnu/patch',
                'tool/gnu/which',
                'tool/gnu/coreutils',
                'tool/gnu/findutils',
                'tool/gnu/diffutils',
                'shell/dash/minimal',
                'stdenv/comp',
                'env/bootstrap',
            ],
        },
    }
