from jinja2 import Environment, FileSystemLoader

env = Environment(loader = FileSystemLoader('./template'))

tmpl = env.get_template('base_config.j2')

data = {
    'host': 'Tokyo_Router',
    'secret_pass': 'san-fran',
    'ip_address': '10.1.1.1',
    'mask': '255.255.255.0',
    'console_pass': 'sanjose',
}

config = tmpl.render(data)

print(config)