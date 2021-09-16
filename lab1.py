#1
NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"
print(NAT.replace('Fast', 'Gigabit'))

#2
MAC = 'AAAA:BBBB:CCCC'
print(MAC.replace(':', '.'))

#3
CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'
print((CONFIG.split())[-1].split(','))
#4
command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'
vlan1 = set((command1.split())[-1].split(','))
vlan2 = set((command2.split())[-1].split(','))
print(list(vlan1.intersection(vlan2)))

#5
VLANS = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
print(sorted(list(set(VLANS))))

#6
ospf_route = 'O            10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
r = ospf_route.split()
dict = {
       "Protocol": "OSPF",
       "Prefix": r[1],
       "AD/Metric": r[2][1:-1],
       "Next-Hop": r[4][:-1],
       "Last update": r[5][:-1],
       "Outbound Inteface": r[6]
}
for x, y in dict.items():
  print("{0:30} {1}".format(x+':',y))
#7
MAC = 'AAAA:BBBB:CCCC'
print(bin(int((''.join(MAC.split(':'))), 16)))
#8
IP = '192.168.3.1'
i1, i2, i3, i4 = IP.split('.')

print("{:10}{:10}{:10}{:10}\n".format(i1, i2, i3, i4)+
      "{:b}{:10b}{:4b}{:9b}".format(int(i1), int(i2), int(i3), int(i4)))
#9
num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']
a = 30
print(len(num_list) - 1 - num_list[::-1].index(a))