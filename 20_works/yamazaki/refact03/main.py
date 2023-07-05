import csv
from network_manager import create_device
from excel_handler import open_excel, save_excel
from cisco_ios.show_interfaces import execute_show_interfaces
from cisco_ios.show_ip_route import execute_show_ip_route

# ホスト情報を読み込む
with open('hosts.csv', 'r') as f:
    reader = csv.DictReader(f)
    hosts = list(reader)

# 各ホストに接続し、情報を取得する
for host in hosts:

    # 接続情報生成
    device = create_device(host)

    # ホストへ接続
    connection = ConnectHandler(**device)

    # enableモードへ移行
    connection.enable()

    # Excelワークブックを開く
    filename = host['filename']
    wb = open_workbook(filename)

    # コマンド実行結果取得とExcelへの出力
    commands = ['show interfaces', 'show ip route']
    for cmd in commands:
        if cmd == 'show interfaces':
            # 必要により個別のワークシートを指定
            ws_interfaces = wb['Tokyo']
            ws_interfaces, row_interfaces = execute_show_interfaces(connection, cmd, ws_interfaces, 17)
        elif cmd == 'show ip route':
            # 必要により個別のワークシートを指定
            ws_routes = wb['Tokyo']
            ws_routes, row_routes = execute_show_ip_route(connection, cmd, ws_routes, 29)

    # エクセルファイルの保存
    save_excel(wb, filename)

    # ホスト接続の解除
    connection.disconnect()

