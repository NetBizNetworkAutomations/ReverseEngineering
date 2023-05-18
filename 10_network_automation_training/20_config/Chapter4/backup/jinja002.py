from jinja2 import Template

tmpl = Template('hostname {{ name }}')

data = {
    'name': 'Tokyo_Router'
}

config = tmpl.render(data)

print(config)