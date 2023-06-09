from netmiko import ConnectHandler
from pprint import pprint

cisco = {
    'device_type': 'cisco_ios_telnet',
    'host': '1.1.1.1',
    'password':'python',
    'secret': 'cisco',
}

net_connect = ConnectHandler(**cisco)

net_connect.enable()

cmd = 'show interfaces'
result = net_connect.send_command(cmd, use_textfsm = True)
pprint(result)

net_connect.disconnect()