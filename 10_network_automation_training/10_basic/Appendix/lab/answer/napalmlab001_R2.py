from napalm import get_network_driver

driver = get_network_driver('ios')

device = driver(
	hostname = '2.2.2.2',
	username = '',
	password = 'python',
	optional_args = {'transport': 'telnet', 'secret': 'cisco'}
)

device.open()

result = device.cli(['show ip route'])

print(result['show ip route'])

with open('R2_ip_route.txt', 'w') as f:
	f.write(result['show ip route'])
	
device.close()