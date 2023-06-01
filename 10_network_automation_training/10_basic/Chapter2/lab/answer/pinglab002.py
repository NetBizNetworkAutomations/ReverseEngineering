import subprocess
import re

hosts = ['100.100.100.100', '192.168.255.100', '192.168.200.2']

for host in hosts:
	p = subprocess.Popen('ping -c5 ' + host, shell=True, stdout = subprocess.PIPE)

	stdout_data, stderr_data = p.communicate()

	result = re.search('ttl', stdout_data.decode('shift_jis'))

	if result:
		print(host + 'へのpingが成功しました')
	else:
		print(host + 'へのpingが失敗しました')