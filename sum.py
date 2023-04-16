a = input('Enter a number:')
b = input('Enter a 2nd number:')
c = input('Enter a 3rd number:')
try:
    if a == b and b == c:
        x = (int(a) + int(b) + int(c)) * 3
    else:
        x = int(a) + int(b) + int(c)
    print(x)
except:
    print ('Enter only numbers')
