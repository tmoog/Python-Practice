num = input('Enter a number: ')
try:
    num = int(num)
    if num > 17:
        diff = (num - 17) * 2
    else:
        diff = num - 17
    print(diff)
except:
    print('Please enter a number')
