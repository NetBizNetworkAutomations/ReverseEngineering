import subprocess

p = subprocess.Popen('ping 10.1.1.254', stdout = subprocess.PIPE)

stdout_data, stderr_data = p.communicate()

print(stdout_data)