from netmiko import ConnectHandler
import csv

cisco = {
	'device_type': 'cisco_ios_telnet',
	'host': '3.3.3.3',
	'password': 'python',
	'secret': 'cisco'
}

net_connect = ConnectHandler(**cisco)
net_connect.enable()

cmd = 'show ip int brief'
results = net_connect.send_command(cmd, use_textfsm = 'True')

for result in results:
	print(result['intf'] + '：' + result['ipaddr'])

with open('show_int.csv', 'w', newline = '') as f:
	field = ['intf', 'ipaddr']
	write = csv.DictWriter(f, fieldnames = field, extrasaction = 'ignore')
	write.writeheader()
	write.writerows(results)

net_connect.disconnect()