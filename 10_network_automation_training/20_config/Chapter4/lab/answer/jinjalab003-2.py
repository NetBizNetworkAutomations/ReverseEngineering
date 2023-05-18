from jinja2 import Environment, FileSystemLoader

env = Environment(loader = FileSystemLoader('./template'))
tmpl = env.get_template('int.j2')

data = {
    'name': 'setagaya_switch',
    'secret_pass': 'san-fran',
    'int': [],
    'console_pass': 'sanjose',
}

int_list = [
    ['gi0/1', '10.1.1.1', '255.255.255.0', 'no shutdown'],
    ['gi0/2', '10.1.2.1', '255.255.255.0', 'no shutdown'],
    ['gi0/3', '10.1.3.1', '255.255.255.0', 'shutdown'],
    ['gi0/4', '10.1.4.1', '255.255.255.0', 'shutdown'],
]

for x in int_list:
    data['int'].append({
        'int_name': x[0],
        'ip_address': x[1],
        'mask': x[2],
        'status': x[3],
    })

config = tmpl.render(data)

with open('int.cfg', 'w') as f:
    f.write(config)