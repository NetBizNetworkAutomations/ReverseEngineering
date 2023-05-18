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

outputs = []

for result in results:
	outputs.append([result['interface'],result['ip_address']])

for output in outputs:
	print(output)

net_connect.disconnect()