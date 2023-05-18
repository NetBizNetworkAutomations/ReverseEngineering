from netmiko import ConnectHandler

cisco = {
	'device_type': 'cisco_ios_telnet',
	'host': '1.1.1.1',
	'password': 'python',
	'secret': 'cisco'
}

net_connect = ConnectHandler(**cisco)
net_connect.enable()

cmd = 'ip route 3.3.3.3 255.255.255.255 172.16.1.2'
net_connect.send_config_set(cmd)

cmd = 'copy running-config startup-config'
net_connect.send_command_timing(cmd)

cmd = '\n'
net_connect.send_command_timing(cmd)

cmd = 'show ip route'
result = net_connect.send_command(cmd)

print(result)

with open('R1_ip_route_toR2.txt', 'w') as f:
	f.write(result)
	
net_connect.disconnect()