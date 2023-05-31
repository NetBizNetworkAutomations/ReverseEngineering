from netmiko import ConnectHandler

cisco = {
	'device_type': 'cisco_ios_telnet',
	'host': '2.2.2.2',
	'password': 'python',
	'secret': 'cisco'
}

net_connect = ConnectHandler(**cisco)
net_connect.enable()

cmd = 'ip route 100.100.100.100 255.255.255.255 192.168.100.254'
net_connect.send_config_set(cmd)

cmd = 'copy running-config startup-config'
net_connect.send_command_timing(cmd)
cmd = '\n'
net_connect.send_command_timing(cmd, delay_factor = 5)

cmd = 'show ip route'
result = net_connect.send_command(cmd)

print(result)

with open('R2_ip_route_after.txt', 'w') as f:
	f.write(result)
	
net_connect.disconnect()