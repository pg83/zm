import os


out = os.environ['out']
sdk = '/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk'

data = r'''
export MACOSX_DEPLOYMENT_TARGET=10.12
export OSX_SDK="{sdk}"
export CPPFLAGS="--sysroot $OSX_SDK -isystem$OSX_SDK/usr/include -F$OSX_SDK -nostdlib++ -Wno-stdlibcxx-not-found"
export LDFLAGS="--sysroot $OSX_SDK -L$OSX_SDK/usr/lib -F$OSX_SDK -nostdlib++ -Wl,-platform_version -Wl,macos -Wl,10.12 -Wl,10.12 -Wl,-no_uuid"
'''.format(sdk=out)

os.chdir(out)

with open('env', 'w') as f:
    f.write(data)

os.symlink(sdk + '/System', 'System')
os.makedirs('usr/lib')
os.symlink(sdk + '/usr/include', 'usr/include')

libs = (
    'libSystem.B.tbd',
    'libSystem.tbd',
    'libc.tbd',
    'libdl.tbd',
    'libm.tbd',
    'libpthread.tbd',
    'libobjc.A.tbd',
    'libresolv.tbd',
    'libutil.tbd',
)

for x in libs:
    os.symlink(sdk + '/usr/lib/' + x, 'usr/lib/' + x)
