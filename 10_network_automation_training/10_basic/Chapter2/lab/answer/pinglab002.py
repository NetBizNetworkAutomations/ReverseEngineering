import subprocess
import re

hosts = ['100.100.100.100', '200.200.200.200', '192.168.200.2']

for host in hosts:
	p = subprocess.Popen('ping ' + host, stdout = subprocess.PIPE)

	stdout_data, stderr_data = p.communicate()

	result = re.search('TTL', stdout_data.decode('shift_jis'))

	if result:
		print(host + 'へのpingが成功しました')
	else:
		print(host + 'へのpingが失敗しました')