import subprocess
import re

hosts = ['100.100.100.100', '200.200.200.200', '192.168.200.2' ]

for host in hosts:
	p = subprocess.Popen('ping ' + host, stdout = subprocess.PIPE)

	stdout_data, stderr_data = p.communicate()
	
	if re.search('TTL', stdout_data.decode('shift_jis')):
		print(host + 'へは到達可能です。')
	elif re.search('到達できません', stdout_data.decode('shift_jis')):
		print(host + 'への経路情報がありません。')
	elif re.search('タイムアウト', stdout_data.decode('shift_jis')):
		print(host + 'は存在しないかフィルタされている可能性があります。')