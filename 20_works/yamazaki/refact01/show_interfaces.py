from netaddr import IPAddress, IPNetwork

def execute_command(connection, cmd, ws, row=17):
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
    
    return ws
