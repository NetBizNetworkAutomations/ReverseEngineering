from jinja2 import Template

tmpl = Template('hostname {{ name }}')

config = tmpl.render(name = 'Tokyo_Router')

print(config)