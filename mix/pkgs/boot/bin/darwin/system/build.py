import os


os.chdir(os.environ['out'])
os.makedirs('bin')
os.chdir('bin')

F = (
    '/usr/bin/lipo',
    '/usr/bin/ld',
    '/usr/bin/install_name_tool',
    '/usr/bin/libtool',
)

for f in F:
    os.symlink(f, os.path.basename(f))
