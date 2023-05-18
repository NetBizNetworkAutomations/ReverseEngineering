from netmiko import ConnectHandler

cisco = {
	'device_type': 'cisco_ios_telnet',
	'host': '1.1.1.1',
	'password': 'python',
	'secret': 'cisco'
}

net_connect = ConnectHandler(**cisco)

net_connect.enable()

cmd = 'show running-config'
result = net_connect.send_command(cmd)

print(result)

net_connect.disconnect()