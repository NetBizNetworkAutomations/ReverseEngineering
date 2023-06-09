"""
このモジュールは、一連のホストから取得した設定情報をエクセルへ反映する機能を提供します
"""
import configparser
from netmiko import ConnectHandler
from network_lib import create_device, load_hosts
from excel_lib import open_workbook, save_excel
from command_executor import execute_commands
from check_lib import check_file_exists

def run_reverse_operations():
    """
    この関数は以下の処理を実施しています
    1. 設定ファイルの読み込み
    2. 設定ファイルで指定されたホスト情報を読み込んで接続
    3. コマンドの実行と結果のパース、エクセルへの反映を含む一連の操作を実行
    """
    # 設定ファイルを読み込む
    config_ini_path = 'config.ini'
    try:
        check_file_exists(config_ini_path)
    except FileNotFoundError as error:
        print(error)
        # ファイルが存在しない場合、ここで処理を終了する
        return
    
    config = configparser.ConfigParser()
    config.read(config_ini_path)

    # ホスト情報を読み込む
    hosts = load_hosts(config['DEFAULT']['HostsCSV'])

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
        execute_commands(connection, wb, config['DEFAULT']['CommandsCSV'])

        # エクセルファイルの保存
        save_excel(wb, filename)

        # ホスト接続の解除
        connection.disconnect()
