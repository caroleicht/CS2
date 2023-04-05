file = open('file.txt')                                 # _io.TextIOWrapper, opens txt file
file = file.read()                                      # str, file
file = file.lower()                                     # str, lowercase letters
file = list(file)                                       # list, list of characters in file

d = dict()                                              # dict, empty dict

for letter in file:                                     # goes through each word in list
    if letter.isalpha():                                # bool, if is a letter and not other character or number
        if letter not in d:                             # bool, if email isn't in dict
            d[letter] = 1                               # int, 1, count of times email occurs
        else:                                           # bool, if email is in dict
            d[letter] = d[letter] + 1                   # int, ex: 2, count of times email occurs
    else:                                               # bool, if is not a letter
        continue                                        # skip character

d = sorted(d.items(), key=lambda x:x[1], reverse=True)  # sorts dict in descending order by val
d = dict(d)                                             # dict

for line in d:                                          # goes throguh lines in dict
    print(f'''{line}: {d[line]}
    ''')                                                # print dict line by line