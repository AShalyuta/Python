#1
print('1')
file = open('ospf.txt', 'r')
ospf_routes = file.readlines()

file.close()

for ospf_route in ospf_routes:
      print("ROUTE {} ".format( str(ospf_routes.index(ospf_route)+1)) )
      ospf_route = ospf_route.replace(',', '')
      ospf_route = ospf_route.replace('[', '')
      ospf_route = ospf_route.replace(']', '')
      ospf_route = ospf_route.replace('via ', '')
      ospf_route = ospf_route.replace('O', 'OSPF')
      ospf_route = ospf_route.split()

      print("Protocol:              {}\n".format(ospf_route[0]) +
            "Prefix:                {}\n".format(ospf_route[1]) +
            "AD/Metric:             {}\n".format(ospf_route[2]) +
            "Next-Hop:              {}\n".format(ospf_route[3]) +
            "Last update:           {}\n".format(ospf_route[4]) +
            "Outbound Interface:    {}".format(ospf_route[5]))
#2
print('2')
file = open('config_sw1.txt', 'r')

for line in file.readlines():
    if not line.startswith('!'):
        print(line.rstrip())

file.close()
#2a
print('2a')
file = open('config_sw1.txt', 'r')
ignore = ['duplex', 'alias', 'Current configuration']

for line in file.readlines():
    if not line.startswith('!'):
        
        in_ignore = False
        
        for item in ignore:
            if line.find(item) != -1:
                in_ignore = True

        if not in_ignore:
            print(line.rstrip())

file.close()
#2b
print('2b')
input_file = open('config_sw1.txt', 'r')
output_file = open('config_sw1_cleared.txt', 'w+')
ignore = ['duplex', 'alias', 'Current configuration']

for line in input_file.readlines():
    if not line.startswith('!'):
        
        in_ignore = False
        
        for item in ignore:
            if line.find(item) != -1:
                in_ignore = True

        if not in_ignore:
            output_file.write(line)

output_file.seek(0)
for line in output_file.readlines():
    print(line.rstrip())

input_file.close()
output_file.close()
#2c
print('2c')
input_file_name = 'config_sw1.txt'
output_file_name = 'config_sw1_cleared.txt'
ignore = ['duplex', 'alias', 'Current configuration']

input_file = open(input_file_name, 'r')
output_file = open(output_file_name, 'w+')

for line in input_file.readlines():
    if not line.startswith('!'):
        
        in_ignore = False
        
        for item in ignore:
            if line.find(item) != -1:
                in_ignore = True

        if not in_ignore:
            output_file.write(line)

output_file.seek(0)
for line in output_file.readlines():
    print(line.rstrip())

input_file.close()
output_file.close()
#3
print('3')
input_file = open("CAM_table.txt", 'r')

input_file_data = input_file.readlines()
input_file_data_processed = []

for line in input_file_data:
    if '.' in line:
        input_file_data_processed.append(line)

for line in input_file_data_processed:
    print(line.rstrip())
#3a
print('3a')
input_file = open("CAM_table.txt", 'r')

input_file_data = input_file.readlines()
input_file_data_processed = []

for line in input_file_data:
    if '.' in line:
        input_file_data_processed.append(line.split())

buffer = []
for i in range(0, len(input_file_data_processed)):
    for j in range(i+1, len(input_file_data_processed)):
        if input_file_data_processed[i][0] > input_file_data_processed[j][0]:
            buffer = input_file_data_processed[i]
            input_file_data_processed[i] = input_file_data_processed[j]
            input_file_data_processed[j] = buffer

for i in range(0, len(input_file_data_processed)):
    input_file_data_processed[i] = '    '.join(input_file_data_processed[i])

for line in input_file_data_processed:
    print(line)
#3b
print('3b')
input_file = open("CAM_table.txt", 'r')

input_file_data = input_file.readlines()
input_file_data_processed = []

chosen_VLAN = int(input("Enter VLAN number: "))

for line in input_file_data:
    if '.' in line and int((line.split())[0]) == chosen_VLAN:
        input_file_data_processed.append(line)

for line in input_file_data_processed:
    print(line.rstrip())