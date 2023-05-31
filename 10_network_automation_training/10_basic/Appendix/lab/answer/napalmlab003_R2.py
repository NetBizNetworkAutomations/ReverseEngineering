from napalm import get_network_driver
import json

driver = get_network_driver('ios')

device = driver(
	hostname = '2.2.2.2',
	username = '',
	password = 'python',
	optional_args = {'transport': 'telnet', 'secret': 'cisco'}
)

device.open()

device.load_merge_candidate(filename = 'napalmlab003_R2.cfg')

print(device.compare_config())

device.commit_config()

result = device.get_interfaces_ip()

print(json.dumps(result, indent = 4))

with open('R2_get_interfaces_ip.txt', 'w') as f:
	json.dump(result, f, indent = 4)

device.close()