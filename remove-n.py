def remove_n(n, string):
    astring = string[:n]
    bstring = string[n+1:]
    nstring = astring + bstring
    return nstring

print(remove_n(3, 'hello'))
