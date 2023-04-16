def match_string(file_name):
    file = open(file_name)
    import re
    for line in file:
        x = re.findall('a.*b$', line)
        if len(x) > 0:
            print(x)

file_name = 'hello.txt'

match_string(file_name)