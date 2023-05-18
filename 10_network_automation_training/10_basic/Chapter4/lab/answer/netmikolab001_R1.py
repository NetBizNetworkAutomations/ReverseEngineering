from netmiko import ConnectHandler

cisco = {
	'device_type': 'cisco_ios_telnet',
	'host': '1.1.1.1',
	'password': 'python',
	'secret': 'cisco'
}

net_connect = ConnectHandler(**cisco)
net_connect.enable()

cmd = 'show ip route'
result = net_connect.send_command(cmd)

print(result)

with open('R1_ip_route.txt', 'w') as f:
	f.write(result)

net_connect.disconnect()