import subprocess
import re

hosts = ['192.168.255.1', '8.8.8.8', '192.168.100.2']

for host in hosts:

	p = subprocess.Popen('ping -c5 ' + host, shell=True, stdout = subprocess.PIPE)

	stdout_data, stderr_data = p.communicate()
	result = re.search('ttl', stdout_data.decode('shift_jis'))

	if result:
		status = 'up'
	else:
		status = 'down'

	print(host + ' is ' + status)
