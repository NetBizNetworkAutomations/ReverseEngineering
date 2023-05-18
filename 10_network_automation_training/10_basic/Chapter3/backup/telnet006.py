from telnetlib import Telnet
WAIT_TIME = 3

tn = Telnet('1.1.1.1')

tn.read_until(b'Password:', WAIT_TIME)
tn.write(b'python\n')

tn.read_until(b'>', WAIT_TIME)
tn.write(b'enable\n')

tn.read_until(b'Password:', WAIT_TIME)
tn.write(b'cisco\n')

tn.read_until(b'#', WAIT_TIME)
tn.write(b'show ip int brief\n')

result = tn.read_until(b'#', WAIT_TIME)
print(result.decode('utf-8'))

tn.write(b'exit\n')