import os


data = '''
export untar="bsdtar xf"
export unzip="unzip"
'''

with open(os.environ['out'] + '/env', 'w') as f:
    f.write(data.strip() + '\n')
