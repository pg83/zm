import os


data = '''
export CPPFLAGS="-isystem/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include"
export LDFLAGS="-L/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/lib"
'''

os.chdir(os.environ['out'])

with open('env', 'w') as f:
    f.write(data)
