def package(mix):
    return {
        'build': {
            'script': mix.files.build_sh,
            'fetch': [
                {
                    'url': 'https://github.com/elfmz/far2l/archive/cfb97146424e739966d8fc53ee832a4a1cc0e685.zip',
                    'md5': '26e676988fa5b47ed211281e6140d371',
                },
            ],
            'depends': [
                'lib/ssh',
                'lib/pcre',
                'lib/spdlog',
                'lib/archive',
                'lib/xerces-c',
                'lib/uchardet',
                'dev/build/pkg-config',
                'dev/build/cmake',
                'dev/lang/m4',
                'stdenv',
            ],
        },
    }
