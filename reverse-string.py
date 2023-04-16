def reverse_string(str):
    rstr = ''
    index = len(str)
    while index > 0:
        rstr += str[index - 1]
        index = index - 1
    return rstr
print(reverse_string('1234abcd'))