import subprocess
import re
import csv

with open('ip.csv') as f:
	hosts = csv.DictReader(f)

	for host in hosts:

		p = subprocess.Popen('ping -c5 ' + host['ip'], shell=True, stdout = subprocess.PIPE) 
		stdout_data, stderr_data = p.communicate()
		result = re.search('ttl',stdout_data.decode('shift_jis'))
        
		if result:
			status = 'up'
		else:
			status = 'down'

		print(host['ip'] + ' is ' + status)