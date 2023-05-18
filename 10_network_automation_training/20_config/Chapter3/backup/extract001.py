from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios_telnet',
    'host': '10.1.1.254',
    'password': 'python',
    'secret': 'cisco',
}

net_connect = ConnectHandler(**device)

net_connect.enable()
cmd = 'show running-config'
result = net_connect.send_command(cmd)

net_connect.disconnect()

print(result)