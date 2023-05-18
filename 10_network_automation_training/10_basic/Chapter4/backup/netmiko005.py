from netmiko import ConnectHandler

cisco = {
	'device_type': 'cisco_ios_telnet',
	'host': '1.1.1.1',
	'password': 'python',
	'secret': 'cisco'
}

net_connect = ConnectHandler(**cisco)

net_connect.enable()

cmd = 'copy running-config startup-config'
net_connect.send_command_timing(cmd)

cmd = '\n'
net_connect.send_command_timing(cmd)

net_connect.disconnect()