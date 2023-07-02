from openpyxl import load_workbook
from netmiko import ConnectHandler
from textfsm import TextFSM
from netaddr import IPAddress, IPNetwork
import csv

# ホスト情報を読み込む
with open('hosts.csv', 'r') as f:
    reader = csv.reader(f)
    hosts = list(reader)

# Excelワークブックを開く
filename = 'sample2.xlsx'
wb = load_workbook(filename)
ws = wb['Tokyo']

# 各ホストに接続し、情報を取得する
for host in hosts:
    device = {
    'device_type': 'cisco_ios_telnet',
    'host': host[1],
    'password': host[2],
    'secret': host[3],
    }

    connection = ConnectHandler(**device)
    
    connection.enable()
    
    cmd = 'show interfaces'
    output = connection.send_command(cmd, use_textfsm = True)

    # 取得したデータをExcelに出力する
    row = 17
    for x in output:
        emp = '-'
        ws.cell(row, 2).value = x['interface']
        ws.cell(row, 3).value = x['link_status']
        
        if x['ip_address']:
            address = IPNetwork(x['ip_address'])
            ws.cell(row, 4).value = str(address.ip)
            ws.cell(row, 5).value = str(address.netmask)
        else:
            ws.cell(row, 4).value = emp
            ws.cell(row, 5).value = emp
        
        row +=1    
    
    wb.save(filename)
    connection.disconnect()
