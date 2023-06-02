from telnetlib import Telnet
import csv

WAIT_TIME = 3
WAIT_TIME2 = 10

with open('ip.csv') as f:
	hosts = csv.DictReader(f)

	for host in hosts:
		tn = Telnet(host['ip'])

		tn.read_until(b'Password:', WAIT_TIME)
		tn.write(host['password'].encode() + '\n'.encode())

		tn.read_until(b'>', WAIT_TIME)
		tn.write(b'terminal length 0\n')

		tn.read_until(b'>', WAIT_TIME)
		tn.write(b'enable\n')

		tn.read_until(b'Password:', WAIT_TIME)
		tn.write(host['secret'].encode() + '\n'.encode())

		tn.read_until(b'#', WAIT_TIME)
		tn.write(b'show running-config\n')

		result = tn.read_until(b'#', WAIT_TIME2)

		with open(host['hostname'] + '.cfg', 'w', newline = '\n') as f:
			f.write((result.decode('utf-8')))

			tn.write(b'exit\n')