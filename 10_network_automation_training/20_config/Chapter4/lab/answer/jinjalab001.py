from jinja2 import Environment, FileSystemLoader

env = Environment(loader = FileSystemLoader('./template'))
tmpl = env.get_template('router.j2')

config = tmpl.render(
    name = 'komazawa_rt',
    secret_pass = 'cisco_koma',
    ntp = '10.1.1.1',
    vty_pass = 'sanjose_koma'
)

with open('router.cfg', 'w') as f:
    f.write(config)