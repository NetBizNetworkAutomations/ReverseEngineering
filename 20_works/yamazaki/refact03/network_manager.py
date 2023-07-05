def create_device(host):
    return {
        'device_type': 'cisco_ios_telnet',
        'host': host['ip'],
        'password': host['password'],
        'secret': host['secret'],
    }
