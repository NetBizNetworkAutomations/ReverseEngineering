from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios_telnet',
    'host': '192.168.255.100',
    'password': 'python',
    'secret': 'cisco',
}

net_connect = ConnectHandler(**device)

net_connect.enable()

cmd = 'show version'
result = net_connect.send_command(cmd, use_textfsm = True)

for x in result:
    print(x['hardware'][0])

net_connect.disconnect()