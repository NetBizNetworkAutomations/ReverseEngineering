import subprocess

p = subprocess.Popen('ping 10.1.1.254', stdout = subprocess.PIPE)

stdout_data, stderr_data = p.communicate()
	
print('以下はstdout_data変数の内容の出力です')
print(stdout_data.decode('shift_jis'))
