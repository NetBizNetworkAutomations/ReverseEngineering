from netmiko import ConnectHandler

hosts = [
			{'hostname':'R2','ip address':'192.168.255.246'},
			{'hostname':'R1','ip address':'192.168.255.52'},
		]

for host in hosts:
	cisco = {
		'device_type': 'cisco_ios_telnet',
		'host': host['ip address'],
		'password': 'python',
		'secret': 'cisco',
	}

	print(host['hostname'] + 'への接続を開始します・・・')
	
	net_connect = ConnectHandler(**cisco)

	net_connect.enable()
	
	print(host['hostname'] + 'で初期化用の設定をstartup-configへコピーします')

	cmd = 'copy flash:python_init.cfg startup-config'
	net_connect.send_command_timing(cmd,)
	net_connect.send_command_timing('\n', delay_factor = 5)

	print(host['hostname'] + 'を再起動します・・・')
	cmd = 'reload'
	result = net_connect.send_command_timing(cmd)

	if 'confirm' in result:
		net_connect.send_command_timing('\n')
	elif 'System' in result:
		net_connect.send_command_timing('no')
		net_connect.send_command_timing('\n')
	else:
		print('再起動に失敗しました')
	
	print('-'*50)

print('スクリプトが終了しました。\nデバイスが起動するまでしばらくお待ちください')