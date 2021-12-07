#1
access_dict = {  'FastEthernet0/12':10,
                'FastEthernet0/14':11,
                'FastEthernet0/16':17,
                'FastEthernet0/17':150
             }

def generate_access_config(access):
    access_template = [ 'switchport mode access',
                        'switchport access vlan',
                        'switchport nonegotiate',
                        'spanning-tree portfast',
                        'spanning-tree bpduguard enable']
    access_conf = []
    for interface, vlan in access_dict.items():
        access_conf.append('interface {}'.format(interface))
        access_template_copy = access_template.copy()
        access_template_copy[1] += " {}".format(vlan)
        access_conf += access_template_copy
    return access_conf

for string in generate_access_config(access_dict):
    print(string)
#1A
print('1A')
access_dict = {  'FastEthernet0/12':10,
                'FastEthernet0/14':11,
                'FastEthernet0/16':17,
                'FastEthernet0/17':150
             }

def generate_access_config(access, psecurity=False):
    access_template = [ 'switchport mode access',
                        'switchport access vlan',
                        'switchport nonegotiate',
                        'spanning-tree portfast',
                        'spanning-tree bpduguard enable']
    port_security = ['switchport port-security maximum 2',
                     'switchport port-security violation restrict',
                     'switchport port-security']
    access_conf = []
    for interface, vlan in access_dict.items():
        access_conf.append('interface {}'.format(interface))
        access_template_copy = access_template.copy()
        access_template_copy[1] += " {}".format(vlan)
        access_conf += access_template_copy
        if psecurity:
            access_conf += port_security
    return access_conf

for string in generate_access_config(access_dict, psecurity=True):
    print(string)
#1B
print('1B')
def generate_access_config(access, psecurity=False):
    access_template = ['switchport mode access',
                   'switchport access vlan',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

    port_security = ['switchport port-security maximum 2',
                     'switchport port-security violation restrict',
                     'switchport port-security']
    finish = {}
    for inter, vlan in access.items():
        finish[inter]=[]
        for config in access_template:
            if config.endswith('access vlan'):
                finish[inter].append(config + ' {}'.format(vlan))
            else:
                finish[inter].append(config)
        for security in port_security:
            if psecurity:
                finish[inter].append(security)
    print(finish)
    return finish

access_dict = { 'FastEthernet0/12':10,
                'FastEthernet0/14':11,
                'FastEthernet0/16':17,
                'FastEthernet0/17':150 }

generate_access_config(access_dict, psecurity=True)
#2
print('2')
trunk_dict = {  'FastEthernet0/1':[10,20],
                'FastEthernet0/2':[11,30],
                'FastEthernet0/4':[17]
             }


def gen_trunk_conf(trunk):
    trunk_template = ['switchport trunk encapsulation dot1q',
                      'switchport mode trunk',
                      'switchport trunk native vlan 999',
                      'switchport trunk allowed vlan']
    trunk_conf = []
    for interface, vlan in trunk_dict.items():
        trunk_conf.append('interface {}'.format(interface))
        trunk_template_copy = trunk_template.copy()
        trunk_template_copy[3] += " {}".format(", ".join([str(i) for i in vlan]))
        trunk_conf += trunk_template_copy
    return trunk_conf

for string in gen_trunk_conf(trunk_dict):
    print(string)
#2A
print('2A')
trunk_dict = {  'FastEthernet0/1':[10,20],
                'FastEthernet0/2':[11,30],
                'FastEthernet0/4':[17]
             }


def gen_trunk_conf(trunk):
    trunk_template = ['switchport trunk encapsulation dot1q',
                      'switchport mode trunk',
                      'switchport trunk native vlan 999',
                      'switchport trunk allowed vlan']
    trunk_conf_dict = {}

    for interface, vlan in trunk_dict.items():
        trunk_conf = []
        trunk_template_copy = trunk_template.copy()
        trunk_template_copy[3] += " {}".format(", ".join([str(i) for i in vlan]))
        trunk_conf += trunk_template_copy
        trunk_conf_dict.update({interface: trunk_conf})
    return trunk_conf_dict

for key, value in gen_trunk_conf(trunk_dict).items():
    print(key, value)
#3
print('3')
def get_int_vlan_map(config):
    with open(config, 'r') as file:
            access_config = {}
            trunk_config = {}
            for line in file:
                if line.find('FastEthernet') != -1:
                    interface = line.split()[-1]
                elif line.find('access vlan') != -1:
                    access_vlan = line.split()[-1]
                    access_config[interface] = access_vlan
                elif line.find('trunk allowed vlan') != -1:
                    trunk_vlan = line.split()[-1]
                    trunk_config[interface] = trunk_vlan
                else:
                    pass
            print('access interfaces: \n', access_config)
            print('trunk interfaces: \n', trunk_config)
    return access_config, trunk_config
get_int_vlan_map('config_sw1.txt')
#3A
print('3A')
def get_int_vlan_map(config):
    access_config = {}
    trunk_config = {}
    with open(config, 'r') as file:
        for line in file:
            if line.find('FastEthernet') != -1:
                interface = line.split()[-1]
                line = file.readline()
                if line.find('mode access') != -1:
                    line = file.readline()
                    access_vlan = line.split()[-1]
                    if access_vlan.isdigit():
                        access_config[interface] = access_vlan
                    else:
                        access_config[interface] = '1'
                elif line.find('encapsulation dot1q') != -1:
                    line = file.readline()
                    trunk_vlan = line.split()[-1]
                    test_t = trunk_vlan
                    trunk_config[interface] = trunk_vlan
        print('access interfaces: \n', access_config)
        print('trunk interfaces: \n', trunk_config)
        return access_config, trunk_config
get_int_vlan_map('config_sw2.txt')
#4
print('4')
ignore = ['duplex', 'alias', 'Current configuration']

def ignore_command(command, ignore):
    """
    Функция проверяет содержится ли в команде слово из списка ignore.
    command - строка. Команда, которую надо проверить
    ignore - список. Список слов
    Возвращает True, если в команде содержится слово из списка ignore, False - если нет
    """
    ignore_command = False
    for word in ignore:
        if word in command:
            return True
    return ignore_command

def config_to_dict(config):
    input_config = []
    output_dict = {}
    with open(config, 'r') as f:
        input_config = [s.rstrip() for s in f.readlines()]
    
    for s in range(0, len(input_config)):
        value_list = []
        key = ""
        if not input_config[s].startswith((' ', '!')) and not ignore_command(input_config[s], ignore):
            key = input_config[s]
            for ss in range(s+1, len(input_config)):
                if not input_config[ss].startswith(' '):
                    s = ss-1
                    break
                else:
                    value_list.append(input_config[ss].strip())
        output_dict.update({key: value_list})
        ++s
    return output_dict

for key, value in config_to_dict('config_sw1.txt').items():
    print ("{}: {}".format(key, str(value)))
