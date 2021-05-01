from jinja2 import Template

tmpl = Template(u'''\
<html>
<head><title>{{ variable|escape }}</title></head>
<body>
{% for item in item_list %}
   {{ item }}{% if not loop.last %},{% endif %}
{% endfor %}
</body>
</html>'''
)

print(tmpl.render(variable='Value with <unsafe> data', item_list=[1, 2, 3, 4, 5, 6]))
