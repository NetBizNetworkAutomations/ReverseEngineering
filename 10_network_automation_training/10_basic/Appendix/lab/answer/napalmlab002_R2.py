from napalm import get_network_driver

driver = get_network_driver('ios')

device = driver(
	hostname = '2.2.2.2',
	username = '',
	password = 'python',
	optional_args = {'transport': 'telnet', 'secret': 'cisco'}
)

device.open()

device.load_merge_candidate(filename = 'napalmlab002_R2.cfg')

print(device.compare_config())

device.commit_config()

result = device.cli(['show ip route'])

print(result['show ip route'])

with open('R2_ip_route_after.txt', 'w') as f:
	f.write(result['show ip route'])

device.close()