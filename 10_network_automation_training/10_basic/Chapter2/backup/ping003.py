import subprocess
import re

p = subprocess.Popen('ping -c5 192.168.255.2', shell=True, stdout = subprocess.PIPE)

stdout_data, stderr_data = p.communicate()
result = re.search('ttl', stdout_data)