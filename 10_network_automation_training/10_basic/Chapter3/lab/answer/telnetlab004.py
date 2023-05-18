from telnetlib import Telnet
import csv

WAIT_TIME = 3

with open('list.csv', 'r') as f:
	hosts = csv.DictReader(f)
	
	for host in hosts:
		tn = Telnet(host['ip address'])
				
		tn.read_until(b'Password:', WAIT_TIME)
		tn.write(host['vty'].encode() + '\n'.encode())
				
		tn.read_until(b'>', WAIT_TIME)
		tn.write(b'terminal length 0\n')
			
		tn.read_until(b'>', WAIT_TIME)
		tn.write(b'enable\n')

		tn.read_until(b'Password:', WAIT_TIME)
		tn.write(host['enable'].encode() + '\n'.encode())
				
		tn.read_until(b'#', WAIT_TIME)
		tn.write(b'configure terminal\n')
				
		tn.read_until(b'(config)#', WAIT_TIME)
		tn.write(b'int loopback 0\n')

		tn.read_until(b'(config-if)#', WAIT_TIME)
		tn.write(b'description "This is Test"\n')

		tn.read_until(b'(config-if)#', WAIT_TIME)
		tn.write(b'end\n')

		tn.read_until(b'#', WAIT_TIME)
		tn.write(b'show int description\n')

		result = tn.read_until(b'#', WAIT_TIME)

		with open(host['RouterName'] + '-desc.txt', 'w', newline = '\n') as f:
			f.write(result.decode('utf-8'))

		tn.write(b'exit\n')