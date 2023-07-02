from netaddr import IPAddress, IPNetwork

def execute_show_interfaces(connection, cmd, ws, row):
    # コマンド実行結果取得
    output = connection.send_command(cmd, use_textfsm=True)

    # 取得したデータをExcelに出力する
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
        
        row += 1
    
    return ws, row

def execute_show_version(connection, cmd, ws, row):
    # ここに 'another command' の実行と結果の処理を書く
    # 以下はダミーのコード
    # output = connection.send_command(cmd, use_textfsm=True)
    # outputの処理を書く
    return ws, row

def execute_commands(connection, commands, ws):
    for cmd in commands:
        if cmd == 'show interfaces':
            ws, row = execute_show_interfaces(connection, cmd, ws, 17)
        elif cmd == 'show version':
            ws, row = execute_show_version(connection, cmd, ws, 10)
        # 他のコマンドに対応する場合は、elif節を追加する
    return ws
