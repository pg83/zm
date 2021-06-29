DATA = r'''
{% include 'build.sh' %}
'''

{% include 'boot/scripts/build.py' %}


os.chdir(os.environ['out'])
os.makedirs('bin')
os.chdir('bin')
os.symlink('../bmake/bmake', 'bmake')


for x in ('uname', 'sed'):
    with open(x, 'w') as f:
        pass

    os.chmod(x, 0o755)
