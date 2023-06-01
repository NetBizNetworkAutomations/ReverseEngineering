import subprocess
import re

p = subprocess.Popen('ping -c5 8.8.8.8', shell=True, stdout = subprocess.PIPE)

stdout_data, stderr_data = p.communicate()

result = re.search('ttl', stdout_data.decode('shift_jis'))

if result:
	print('8.8.8.8へのpingが成功しました')
else:
	print('8.8.8.8へのpingが失敗しました')