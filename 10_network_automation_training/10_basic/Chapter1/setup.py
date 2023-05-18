from netmiko import ConnectHandler
import csv

with open('device_list.csv', 'r') as fin:
	hosts = csv.DictReader(fin)
	
	for host in hosts:
		cisco = {
			'device_type': 'cisco_ios_telnet',
			'host': host['ip address'],
			'password': host['telnet password'],
			'secret': host['secret password'],
		}
	
		print('-'*80)
		
		print('{0}へ接続します'.format(host['hostname']))
		net_connect = ConnectHandler(**cisco)
		net_connect.enable()
		
		# running-configのバックアップ
		print('{0}の変更前の設定をファイルに保存します'.format(host['hostname']))
		cmd = 'show running-config'
		result = net_connect.send_command_timing(cmd)
		with open(host['hostname'] + '-config_before.cfg', 'w') as fout:
			fout.write(result)
		
		# NTPやsyslogなど基本的な設定の追加追加
		print('{0}へNTPなどの基本的な設定を追加します'.format(host['hostname']))
		cmd = [
				'clock timezone JST 9',
				'ntp server 192.168.100.254',
				'service timestamps debug datetime msec localtime',
				'service timestamps log datetime msec localtime',
			]
		net_connect.send_config_set(cmd)

		# スタティックルート追加前の確認
		print('{0}の確認のため変更前に[show ip route]を実行します'.format(host['hostname']))
		print('-'*80)
		cmd = 'show ip route'
		result = net_connect.send_command(cmd)
		print(result)
		with open(host['hostname'] + '-route_before.cfg', 'w') as fout:
			fout.write(result)
		print('-'*80)
		
		# スタティックルートの追加
		print('{0}へスタティックルートを追加します'.format(host['hostname']))
		if host['hostname'] == 'R1':
			cmd = [
					'ip route 192.168.100.0 255.255.255.0 172.16.1.2',
					'ip route 192.168.200.0 255.255.255.0 172.16.1.2',
					'ip route 2.2.2.2 255.255.255.255 172.16.1.2',
					'ip route 200.200.200.200 255.255.255.255 172.16.1.2',
			]
		elif host['hostname'] == 'R2':
			cmd = [
					'ip route 1.1.1.1 255.255.255.255 172.16.1.1',
					'ip route 192.168.200.0 255.255.255.0 192.168.100.254',
					'ip route 200.200.200.200 255.255.255.255 192.168.100.254',
			]
		net_connect.send_config_set(cmd)
		
		# スタティックルート追加後の確認
		print('{0}の確認のため変更後に[show ip route]を実行します'.format(host['hostname']))
		print('-'*80)
		cmd = 'show ip route'
		result = net_connect.send_command(cmd)
		print(result)
		with open(host['hostname'] + '-route_after.cfg', 'w') as fout:
			fout.write(result)
		print('-'*80)
		
		# インタフェース変更前の確認
		print('{0}の確認のため変更前に[show ip int breif]を実行します'.format(host['hostname']))
		print('-'*80)
		cmd = 'show ip int brief'
		result = net_connect.send_command(cmd)
		print(result)
		with open(host['hostname'] + '-int_before.cfg', 'w') as fout:
			fout.write(result)
		print('-'*80)
		
		# loopback0の追加
		print('{0}へloopback0の設定を追加します'.format(host['hostname']))
		if host['hostname'] == 'R1':
			cmd = ['int lo 0', 'ip add 1.1.1.1 255.255.255.255', 'no shut']
		elif host['hostname'] == 'R2':
			cmd = ['int lo 0', 'ip add 2.2.2.2 255.255.255.255', 'no shut']
		net_connect.send_config_set(cmd)
		
		# インタフェース変更後の確認
		print('{0}の確認のため変更後に[show ip int breif]を実行します'.format(host['hostname']))
		print('-'*80)
		cmd = 'show ip int brief'
		result = net_connect.send_command(cmd)
		print(result)
		with open(host['hostname'] + '-int_after.cfg', 'w') as fout:
			fout.write(result)
		print('-'*80)
		
		# 設定の保存
		print('{0}の設定を保存します'.format(host['hostname']))
		cmd = 'copy running-config startup-config'
		net_connect.send_command_timing(cmd)
		cmd = '\n'
		net_connect.send_command_timing(cmd, delay_factor = 3)
		
		# 設定変更後のrunning-configのバックアップ
		print('{0}の変更後の設定をファイルに保存します'.format(host['hostname']))
		cmd = 'show running-config'
		result = net_connect.send_command_timing(cmd)
		with open(host['hostname'] + '-config_after.cfg' , 'w') as fout:
			fout.write(result)
		
		# デバイスからのログアウト
		print('{0}からログアウトします'.format(host['hostname']))
		net_connect.disconnect()