def remove_leading_zeros(file_name):
    file = open(file_name)
    import re
    for line in file:
        x = re.sub('\.[0]*', '.', line)
        print(x)

file_name = 'hello.txt'

remove_leading_zeros(file_name)