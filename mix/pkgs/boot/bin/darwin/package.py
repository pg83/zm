def package(mix):
    return {
        'runtime': {
            'depends': ['boot/bin/darwin/' + x for x in ('dash', 'clang', 'system')],
        },
    }
