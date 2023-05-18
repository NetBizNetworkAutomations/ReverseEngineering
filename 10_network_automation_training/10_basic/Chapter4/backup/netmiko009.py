from netmiko import ConnectHandler

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

for result in results:
	print('Interface：{0}, IP address：{1}'.format(result['interface'],result['ip_address']))
	
net_connect.disconnect()	