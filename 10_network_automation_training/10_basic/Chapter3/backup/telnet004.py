from telnetlib import Telnet

tn = Telnet('1.1.1.1')

tn.read_until(b'Password:')
tn.write(b'python\n')

tn.read_until(b'>')
tn.write(b'exit\n')