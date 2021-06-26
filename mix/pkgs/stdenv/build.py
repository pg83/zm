import os


data = r'''
export untar="bsdtar xf"
export unzip="unzip"
'''

with open(os.environ['out'] + '/env', 'w') as f:
    f.write(data.strip() + '\n')
