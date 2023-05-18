from telnetlib import Telnet

WAIT_TIME = 3

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
tn.write(b'configure terminal\n')
		
tn.read_until(b'(config)#', WAIT_TIME)
tn.write(b'hostname BranchRouter\n')

tn.read_until(b'(config)#', WAIT_TIME)
tn.write(b'exit\n')

tn.read_until(b'#', WAIT_TIME)
tn.write(b'exit\n')