from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios_telnet',
    'host': '192.168.255.100',
    'password': 'python',
    'secret': 'cisco',
}

net_connect = ConnectHandler(**device)

net_connect.enable()
cmd = 'show running-config'
result = net_connect.send_command(cmd)

net_connect.disconnect()

contents = result.splitlines()

for content in contents:
    if 'timezone' in content:
        print(content.split()[2])