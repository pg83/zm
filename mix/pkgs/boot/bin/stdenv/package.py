def package(mix):
    deps = [
        #'boot/bin/darwin',
        'boot/bin/mix',
    ]

    return {
        'build': {
            'script': mix.files.build_py,
            'depends': deps,
        },
        'runtime': {
            'depends': deps + [
                'env/bootstrap',
            ],
        },
    }
