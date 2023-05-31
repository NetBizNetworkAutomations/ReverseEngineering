from telnetlib import Telnet

tn = Telnet('1.1.1.1')
tn.write(b'python\n')

tn.write(b'exit\n')
