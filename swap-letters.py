def swap_letters(string):
    char1 = string[0]
    char2 = string[-1]
    index = len(string) - 1
    nstring = char2 + string[1:index] + char1
    return nstring

print(swap_letters('hello'))