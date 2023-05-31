from jinja2 import Environment, FileSystemLoader

env = Environment(loader = FileSystemLoader('./template'))
tmpl = env.get_template('int.j2')

data = {
    'name': 'setagaya_switch',
    'secret_pass': 'san-fran',
    'console_pass': 'sanjose',
    'int': [{
        'int_name': 'gi0/1',
        'ip_address': '10.1.1.1',
        'mask': '255.255.255.0',
        'status': 'no shutdown',
    },{
        'int_name': 'gi0/2',
        'ip_address': '10.1.2.1',
        'mask': '255.255.255.0',
        'status': 'no shutdown',
    },{
        'int_name': 'gi0/3',
        'ip_address': '10.1.3.1',
        'mask': '255.255.255.0',
        'status': 'shutdown',
    },{
        'int_name': 'gi0/4',
        'ip_address': '10.1.4.1',
        'mask': '255.255.255.0',
        'status': 'shutdown',
    }],
}

config = tmpl.render(data)

with open('int.cfg', 'w') as f:
    f.write(config)