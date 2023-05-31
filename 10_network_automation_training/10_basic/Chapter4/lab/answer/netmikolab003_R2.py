from netmiko import ConnectHandler

cisco = {
	'device_type': 'cisco_ios_telnet',
	'host': '2.2.2.2',
	'password': 'python',
	'secret': 'cisco'
}

net_connect = ConnectHandler(**cisco)
net_connect.enable()

cmd = [
		'int loopback 3',
		'ip address 3.3.3.3 255.255.255.255',
		'description "management int"'
]

net_connect.send_config_set(cmd)

cmd = 'copy running-config startup-config'
net_connect.send_command_timing(cmd)

cmd = '\n'
net_connect.send_command_timing(cmd)

cmd = 'show int loopback3'
result = net_connect.send_command(cmd)

print(result)

with open('R2_loopback3.txt', 'w') as f:
	f.write(result)
	
net_connect.disconnect()