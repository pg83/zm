import os


data = r'''
{{mix.files.build_sh.data}}
'''

with open(os.environ['out'] + '/env', 'w') as f:
    f.write(data)
