def sequence_finder(file_name):
    file = open(file_name)
    import re
    for line in file:
        x = re.findall('([A-Z][a-z]+)', line)
        if len(x) > 0:
            print(x)

file_name = 'hello.txt'
sequence_finder(file_name)

