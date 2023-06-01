import subprocess
import csv
import re

with open('list.csv', 'r') as f:
	hosts = csv.DictReader(f)	

	for host in hosts:
		p = subprocess.Popen('ping -c5 ' + host['ip address'], shell=True, stdout = subprocess.PIPE)

		stdout_data, stderr_data = p.communicate()
		
		if re.search('ttl', stdout_data.decode('shift_jis')):
			print(host['RouterName'] + 'へは到達可能です。')
		elif re.search('到達できません', stdout_data.decode('shift_jis')):
			print(host['RouterName'] + 'への経路情報がありません。')
		elif re.search('100% packet loss', stdout_data.decode('shift_jis')):
			print(host['RouterName'] + 'は存在しないかフィルタされている可能性があります。')