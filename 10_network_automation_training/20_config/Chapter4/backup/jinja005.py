from jinja2 import Environment, FileSystemLoader

env = Environment(loader = FileSystemLoader('./template'))
tmpl = env.get_template('switch_config.j2')

data = [
    {'name': 'gi0/1', 'vlan': '100'},
    {'name': 'gi0/2', 'vlan': '200'},
    {'name': 'gi0/3', 'vlan': '300'},
    {'name': 'gi0/4', 'vlan': '400'},
]

config = tmpl.render({'name': 'Tokyo_Router', 'int': data})

print(config)