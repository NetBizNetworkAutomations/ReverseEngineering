import subprocess
import re

p = subprocess.Popen('ping 200.200.200.200', stdout = subprocess.PIPE)

stdout_data, stderr_data = p.communicate()

result = re.search('TTL', stdout_data.decode('shift_jis'))

if result:
	print('200.200.200.200へのpingが成功しました')
else:
	print('200.200.200.200へのpingが失敗しました')