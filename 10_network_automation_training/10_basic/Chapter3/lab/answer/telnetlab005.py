from telnetlib import Telnet
import csv

WAIT_TIME = 3

def execute_cmd(prompt, cmd):
	tn.read_until(prompt.encode(), WAIT_TIME)
	tn.write(cmd.encode() + '\n'.encode())

with open('list.csv', 'r') as f:
	hosts = csv.DictReader(f)
	
	for host in hosts:
		tn = Telnet(host['ip address'])

		execute_cmd('Password:', host['vty'])

		execute_cmd('>', 'terminal length 0')

		execute_cmd('>', 'enable')

		execute_cmd('Password:', host['enable'])

		execute_cmd('#', 'configure terminal')

		execute_cmd('(config)#', 'int lo 0')

		execute_cmd('(config-if)#', 'description "This is Test"')
		
		execute_cmd('(config-if)#', 'end')

		execute_cmd('#', 'show int description')

		result = tn.read_until(b'#', WAIT_TIME)

		with open(host['RouterName'] + '-desc.txt', 'w', newline = '\n') as f:
			f.write(result.decode('utf-8'))

		tn.write(b'exit\n')