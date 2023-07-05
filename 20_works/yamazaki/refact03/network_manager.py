import csv
from netmiko import ConnectHandler

def create_device(host):
    return {
        'device_type': 'cisco_ios_telnet',
        'host': host['ip'],
        'password': host['password'],
        'secret': host['secret'],
    }

def load_hosts(filepath):
    # ホスト情報を読み込む
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)
