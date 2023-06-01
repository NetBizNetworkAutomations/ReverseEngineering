import subprocess
import re

p = subprocess.Popen('ping -c5 192.168.255.2', shell=True, stdout = subprocess.PIPE)

stdout_data, stderr_data = p.communicate()
result = re.search('TTL', stdout_data.decode('shift_jis'))

if result:
	status = 'up'
else:
	status = 'down'

print('192.168.255.2 is ' + status)
