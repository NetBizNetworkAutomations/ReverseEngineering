from netmiko import ConnectHandler
from pprint import pprint

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

pprint(result)

net_connect.disconnect()