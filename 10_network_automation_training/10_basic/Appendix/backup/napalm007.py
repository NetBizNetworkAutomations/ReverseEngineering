from napalm import get_network_driver
import json

driver = get_network_driver('ios')

device = driver(
	hostname = '1.1.1.1',
	username = '',
	password = 'python',
	optional_args = {'transport': 'telnet', 'secret': 'cisco'}
)

device.open()

output = device.get_interfaces()

print(json.dumps(output, indent = 4))

device.close()
