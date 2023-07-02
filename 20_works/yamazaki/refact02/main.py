from openpyxl import load_workbook
from netmiko import ConnectHandler
from textfsm import TextFSM
import csv
from execute_commands import execute_commands  # モジュールをインポート

# ホスト情報を読み込む
with open('hosts.csv', 'r') as f:
    reader = csv.DictReader(f)
    hosts = list(reader)

# 各ホストに接続し、情報を取得する
for host in hosts:
    
    # Excelワークブックを開く
    filename = host['filename']
    wb = load_workbook(filename)
    ws = wb['Tokyo']
    
    # 接続情報生成
    device = {
    'device_type': 'cisco_ios_telnet',
    'host': host['ip'],
    'password': host['password'],
    'secret': host['secret'],
    }
    
    # ホストへ接続
    connection = ConnectHandler(**device)
    
    # enableモードへ移行
    connection.enable()
    
    # コマンド実行結果取得とExcelへの出力
    commands = ['show interfaces', 'show version']
    ws = execute_commands(connection, commands, ws)
    
    # エクセルファイルの保存
    wb.save(filename)
    
    # ホスト接続の解除
    connection.disconnect()
