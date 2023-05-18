from jinja2 import Environment, FileSystemLoader

env = Environment(loader = FileSystemLoader('./template'))
tmpl = env.get_template('switch.j2')

data = {
    'name': 'komazawa_switch',
    'domain': 'ctct',
    'vtp': 'transparent',
    'stp': 'rapid-pvst',
    'int_name': 'GigabitEthernet0/1',
    'vlan': '500',
    'switchport': 'access',
}

config = tmpl.render(data)

with open('switch.cfg', 'w') as f:
    f.write(config)