import subprocess
import re

p = subprocess.Popen('ping 10.1.1.251', stdout = subprocess.PIPE)

stdout_data, stderr_data = p.communicate()
result = re.search('TTL', stdout_data)