import os

data = r'''
export untar="$exe $mix misc untar"
export unzip="$exe $mix misc unzip"
'''

with open(os.environ['out'] + '/env', 'w') as f:
    f.write(data)
