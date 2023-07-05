from netaddr import IPNetwork

def execute_show_ip_route(connection, cmd, ws, row):
    # コマンド実行結果取得    
    output = connection.send_command(cmd, use_textfsm=True)
    # outputの処理を書く
    
    # 取得したデータをExcelに出力する
    for x in output:
        #ws.cell(row, 2).value = x['protocol']
        ws.cell(row, 2).value = x['network']
        
        mask = IPNetwork('0.0.0.0/' + x['mask'])
        
        ws.cell(row, 3).value = str(mask.netmask)
        ws.cell(row, 4).value = x['nexthop_ip'] or '-'
        #ws.cell(row, 6).value = x['nexthop_if'] or '-'
        
        row += 1

    return ws, row
