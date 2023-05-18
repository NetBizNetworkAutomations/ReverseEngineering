from napalm import get_network_driver
from pprint import pprint

driver = get_network_driver('ios')

device = driver(
	hostname = '1.1.1.1',
	username = '',
	password = 'python',
	optional_args = {'transport': 'telnet', 'secret': 'cisco'}
)
	
device.open()

output = device.get_interfaces()

pprint(output)

device.close()