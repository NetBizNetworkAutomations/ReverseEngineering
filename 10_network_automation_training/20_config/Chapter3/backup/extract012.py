from netaddr import IPNetwork

address = IPNetwork('192.168.200.1/24')

print(address.ip)
print(address.network)
print(address.prefixlen)