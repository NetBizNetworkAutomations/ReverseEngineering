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

def execute_show_ip_route(connection, cmd, ws, row):
    # コマンド実行結果取得    
    output = connection.send_command(cmd, use_textfsm=True)
    # outputの処理を書く
    
    # 取得したデータをExcelに出力する
    for x in output:
        ws.cell(row, 2).value = x['protocol']
        ws.cell(row, 3).value = x['network']
        
        mask = IPNetwork('0.0.0.0/' + x['mask'])
        
        ws.cell(row, 4).value = str(mask.netmask)
        ws.cell(row, 5).value = x['nexthop_ip'] or '-'
        ws.cell(row, 6).value = x['nexthop_if'] or '-'
        
        row += 1

    return ws, row

def execute_commands(connection, commands, ws):
    for cmd in commands:
        if cmd == 'show interfaces':
            ws, row = execute_show_interfaces(connection, cmd, ws, 17)
        elif cmd == 'show ip route':
            ws, row = execute_show_ip_route(connection, cmd, ws, 49)
        # 他のコマンドに対応する場合は、elif節を追加する
    return ws
