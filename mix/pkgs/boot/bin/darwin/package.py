def package(mix):
    return {
        'runtime': {
            'depends': ['boot/bin/darwin/' + x for x in ('sed', 'dash', 'clang', 'system', 'coreutils')],
        },
    }
