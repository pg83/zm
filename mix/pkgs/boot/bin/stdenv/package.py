def package(mix):
    deps = [
        'boot/bin/darwin',
    ]

    return {
        'build': {
            'script': mix.files.build_sh,
            'depends': deps,
        },
        'runtime': {
            'depends': deps + [
                'env/bootstrap',
            ],
        },
    }
