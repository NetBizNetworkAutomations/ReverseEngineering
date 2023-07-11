from netmiko import ConnectHandler
from network_manager import create_device, load_hosts
from excel_handler import open_workbook, save_excel
from command_executor import execute_commands

def run_reverse_operations():
    # ホスト情報を読み込む
    hosts = load_hosts('hosts.csv')

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
        execute_commands(connection, wb, 'commands.csv')

        # エクセルファイルの保存
        save_excel(wb, filename)

        # ホスト接続の解除
        connection.disconnect()