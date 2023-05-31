import subprocess
import re
import csv

with open('ip.csv') as f:
	hosts = csv.DictReader(f)

	for host in hosts:

		p = subprocess.Popen('ping ' + host['ip'], stdout = subprocess.PIPE) 
		stdout_data, stderr_data = p.communicate()
		result = re.search('TTL',stdout_data.decode('shift_jis'))
        
		if result:
			status = 'up'
		else:
			status = 'down'

		print(host['ip'] + ' is ' + status)