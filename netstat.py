#!/usr/bin/env python

import sys

filename = sys.argv[1]
port_checker = sys.argv[2:]

# print(port_checker)
with open(filename, 'r') as f:
    # Read the text of the file
    active_count = []
    unknown_count = []
    for line in f: 
        line_split = line.split(' ')
        # print(line_split)
        clean_list = []
        for item in line_split:
            if item != '':
                clean_list.append(item)


           

        # local_address = (clean_list[3].split(':'))
        if clean_list[0] == 'Active' or clean_list[0] == 'Proto':
            continue

        local_address = (clean_list[3].split(':'))
        port_number = local_address[-1]
        # print(port_number)
        active_port = clean_list[0][:3] + ':' + port_number
        # print(active_port)
        if active_port in port_checker:
            active_count.append(line)
        else:
            unknown_count.append(line)

    # print(active_count)
    # for item in active_count:
    #     print(item.strip())
if len(active_count) != 0:
    print(str(len(active_count)) + ': Allowed services/connections')
    print('Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name')
    for item in active_count:
        print(item.strip())

if len(active_count) != 0 and len(unknown_count) != 0:
    print('')

if len(unknown_count) != 0:
    print(str(len(unknown_count)) + ': Unknown services/connections')
    print('Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name')
    for item in unknown_count:
        print(item.strip())

