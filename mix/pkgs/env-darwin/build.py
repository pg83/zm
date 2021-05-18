import os

out = os.environ['out']
sdk = '/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk'

data = '''
export OSX_SDK="{sdk}"
export CPPFLAGS="--sysroot $OSX_SDK  -isystem$OSX_SDK/usr/include -F$OSX_SDK"
export LDFLAGS="-L$OSX_SDK/usr/lib -nostdlib++"
'''.format(sdk=out)

os.chdir(out)

with open('env', 'w') as f:
    f.write(data)

os.symlink(sdk + '/System', 'System')
os.makedirs('usr/lib')
os.symlink(sdk + '/usr/include', 'usr/include')

for x in ('libSystem.B.tbd', 'libSystem.tbd', 'libc.tbd', 'libdl.tbd', 'libm.tbd', 'libpthread.tbd'):
    os.symlink(sdk + '/usr/lib/' + x, 'usr/lib/' + x)
