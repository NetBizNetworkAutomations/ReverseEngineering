import subprocess
import re

hosts = ['100.100.100.100', '192.168.255.52', '192.168.200.2' ]

for host in hosts:
	p = subprocess.Popen('ping -c5 ' + host, shell=True, stdout = subprocess.PIPE)

	stdout_data, stderr_data = p.communicate()
	
	if re.search('ttl', stdout_data.decode('shift_jis')):
		print(host + 'へは到達可能です。')
	elif re.search('到達できません', stdout_data.decode('shift_jis')):
		print(host + 'への経路情報がありません。')
	elif re.search('100% packet loss', stdout_data.decode('shift_jis')):
		print(host + 'は存在しないかフィルタされている可能性があります。')