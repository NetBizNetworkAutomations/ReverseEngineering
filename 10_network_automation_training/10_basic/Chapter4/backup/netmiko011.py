from netmiko import ConnectHandler
import csv

cisco = {
    'device_type': 'cisco_ios_telnet',
    'host': '1.1.1.1',
    'password':'python',
    'secret': 'cisco',
}

net_connect = ConnectHandler(**cisco)

net_connect.enable()

cmd = 'show interfaces'
results = net_connect.send_command(cmd, use_textfsm = True)

with open('show_int.csv', 'w', newline = '') as f:
	field = ['interface', 'ip_address']
	writer = csv.DictWriter(f, fieldnames = field, extrasaction = 'ignore')
	writer.writeheader()
	writer.writerows(results)

net_connect.disconnect()
