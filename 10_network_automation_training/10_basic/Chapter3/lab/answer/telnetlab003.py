from telnetlib import Telnet

WAIT_TIME = 5

tn = Telnet('1.1.1.1')
		
tn.read_until(b'Password:', WAIT_TIME)
tn.write(b'python\n')
		
tn.read_until(b'>', WAIT_TIME)
tn.write(b'terminal length 0\n')
	
tn.read_until(b'>', WAIT_TIME)
tn.write(b'enable\n')

tn.read_until(b'Password:', WAIT_TIME)
tn.write(b'cisco\n')
	
tn.read_until(b'#', WAIT_TIME)
tn.write(b'show running-config\n')

result = tn.read_until(b'#', WAIT_TIME)

with open('R1-config.cfg', 'w', newline = '\n') as f:
	f.write(result.decode('utf-8'))

tn.write(b'exit\n')