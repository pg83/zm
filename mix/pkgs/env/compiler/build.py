import os


data = r'''
{% include 'build.sh' %}
'''

with open(os.environ['out'] + '/env', 'w') as f:
    f.write(data)
