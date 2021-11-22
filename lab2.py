#1
ip_address = input("IP: ")
ip_address_list = ip_address.split('.')

oct1 = int(ip_address_list[0])

if 1 <= oct1 <= 223:
    print("unicast")
elif 224 <= oct1 <= 239:
    print("multicast")
elif ip_address == "255.255.255.255":
    print("local broadcast")
elif ip_address == "0.0.0.0":
    print("unassigned")
else:
    print("unused")
#1a
try:
    ip_address = input("IP: ")
    ip_address_list = ip_address.split('.')
    
    for oct in ip_address_list:
        if len(oct) > 3 or len(oct) == 0 or int(oct) > 255 or int(oct) < 0:
            error = 3/0 # istead raise smth :)

    oct1 = int(ip_address_list[0])

    if 1 <= oct1 <= 223:
        print("Address type: unicast")
    elif 224 <= oct1 <= 239:
        print("Address type: multicast")
    elif ip_address == "255.255.255.255":
        print("Address type: local broadcast")
    elif ip_address == "0.0.0.0":
        print("Address type: unassigned")
    else:
        print("Address type: unused")

except:
    print("\nIncorrect IPv4 address")
#1b
while True:
    try:
        ip_address = input("[ Enter \"stop\" to stop the program ]\n"
                           "IP: ")
        
        if ip_address == "stop":
            break

        ip_address_list = ip_address.split('.')
        
        for oct in ip_address_list:
            if len(oct) > 3 or len(oct) == 0 or int(oct) > 255 or int(oct) < 0:
                error = 3/0 # istead raise smth :)

        oct1 = int(ip_address_list[0])

        if 1 <= oct1 <= 223  and oct1 != 127:
            print("Address type: unicast")
        elif 224 <= oct1 <= 239:
            print("Address type: multicast")
        elif ip_address == "255.255.255.255":
            print("Address type: local broadcast")
        elif ip_address == "0.0.0.0":
            print("Address type: unassigned")
        elif ip_address == "127.0.0.1":
            print("Address type: loopback")
        else:
            print("Address type: unused")

    except:
        print("Incorrect IPv4 address")
#2
mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']
mac_cisco = []

for mac_address in mac:
    mac_cisco.append( mac_address.replace(':', '.') )

print(mac_cisco)
#3
access_template = [ 'switchport mode access',
                    'switchport access vlan',
                    'spanning-tree portfast',
                    'spanning-tree bpduguard enable']

trunk_template = [  'switchport trunk encapsulation dot1q',
                    'switchport mode trunk',
                    'switchport trunk allowed vlan']

fast_int = {'access':{'0/12':'10','0/14':'11','0/16':'17','0/17':'150'},
            'trunk':{'0/1':['add','10','20'],
                     '0/2':['only','11','30'],
                     '0/4':['del','17']} }

for intf, vlan in fast_int['access'].items():
    print('interface FastEthernet' + intf)
    for command in access_template:
        if command.endswith('access vlan'):
            print(' {} {}'.format(command, vlan))
        else:
            print(' {}'.format(command))

for intf, vlans in fast_int['trunk'].items():
    print('interface FastEthernet' + intf)
    for command in trunk_template:
        if command.endswith("allowed vlan"):
            out_command = ' {}'.format(command)
            if command.endswith("allowed vlan"):
                if vlans[0] == 'only':
                    out_command += " {}".format(','.join(vlans[1:]))
                else:
                    out_command += " {} {}".format(vlans[0], ','.join(vlans[1:]))
            else:
                print(out_command)
            
            print(out_command)
        else:
            print(' {}'.format(command))