n = input('Enter a number: ')
try:
    n = int(n)
    if n <= 1100 and n >= 900:
        print('near 1000')
    elif n <= 2100 and n >= 1900:
        print('near 2000')
    else:
        print('out of range')
except:
    print('Please enter a number')