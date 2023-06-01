import subprocess

p = subprocess.Popen('ping -c5 192.168.255.100', shell=True, stdout = subprocess.PIPE)
	
stdout_data, stderr_data = p.communicate()