file = open('file.txt')                         # _io.TextIOWrapper, opens txt file
file = file.readlines()                         # list, list of lines in file

list = []                                       # list, empty list

for line in file:                               # goes through each line in file
    if 'From:' in line:                         # bool, if line has 'From:'
        continue                                # skips line
    if 'From' in line:                          # bool, only takes 'From:' lines
        line = line.split(' ')                  # list, list of string values on line
        line = line[-2]                         # str, time with hour:minute:second
        line = line.split(':')                  # list, time separated into hour, minute, time
        line = line[0]                          # str, only hour
        list.append(line)                       # list, add line from file to list
        list = sorted(list)                     # list, hours sorted in numerical order

d = dict()                                      # dict, empty dictionary

for item in list:                               # goes through each word in list
    item = item.split(' ')                      # list, splits string into list of words
    for email in item:                          # goes through words in file
        if email not in d:                      # bool, if email isn't in dict
            d[email] = 1                        # int, 1, count of times email occurs
        else:                                   # bool, if email is in dict
            d[email] = d[email] + 1             # int, ex: 2, count of times email occurs

for line in d:                                  # goes throguh lines in dict
    print(f'''{line}: {d[line]}
    ''')                                        # print dict line by line