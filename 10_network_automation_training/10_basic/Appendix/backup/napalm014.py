from napalm import get_network_driver

driver = get_network_driver('ios')

device = driver(
	hostname = '1.1.1.1',
	username = '',
	password = 'python',
	optional_args = {'transport': 'telnet', 'secret': 'cisco'}
)

device.open()

device.load_merge_candidate(filename = 'loopback90.cfg')

print(device.compare_config())

while True:
	s = input('設定を確定しますか？[yes/no]：')
	if s == 'yes' or s == 'y':
		device.commit_config()
		print('設定を確定しました')
		break
	elif s == 'no' or s == 'n':
		device.discard_config()
		print('設定を破棄しました')
		break

device.close()