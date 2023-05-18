import subprocess
import re

hosts = ['10.1.1.254', '192.168.100.1', '192.168.100.2']

for host in hosts:

	p = subprocess.Popen('ping ' + host, stdout = subprocess.PIPE)

	stdout_data, stderr_data = p.communicate()
	result = re.search('TTL', stdout_data.decode('shift_jis'))

	if result:
		status = 'up'
	else:
		status = 'down'

	print(host + ' is ' + status)
