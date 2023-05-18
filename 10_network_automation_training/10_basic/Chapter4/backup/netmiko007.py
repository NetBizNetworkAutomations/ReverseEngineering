from netmiko import ConnectHandler

cisco = {
	'device_type': 'cisco_ios_telnet',
	'host': '1.1.1.1',
	'password': 'python',
	'secret': 'cisco'
}

net_connect = ConnectHandler(**cisco)

net_connect.enable()

cmd = ['int gi0/1', 'description “Connect To PC”']
net_connect.send_config_set(cmd)

net_connect.disconnect()