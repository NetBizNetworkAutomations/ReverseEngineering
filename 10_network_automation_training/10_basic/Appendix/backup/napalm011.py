from napalm import get_network_driver

driver = get_network_driver('ios')

device = driver(
	hostname = '1.1.1.1',
		username = '',
		password = 'python',
		optional_args = {'transport': 'telnet', 'secret': 'cisco'}
)

device.open()

device.load_merge_candidate(filename = 'loopback70.cfg')

device.close()