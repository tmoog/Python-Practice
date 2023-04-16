def prime(n):
    for x in range(2, (int(n) - 1)):
        if n % x == 0:
            return False
        else:
            return True

def prime_checker():
    n = float(input('Enter a number: '))
    if prime(n) == False:
        print('not prime')
    elif prime(n) == True:
        print('prime')

prime_checker()