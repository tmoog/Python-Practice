import random
n = random.randint(1, 9)
print(n)
while True:
    a = int(input('Guess a number 1 through 9: '))
    if n == a:
        print('Well guessed!')
        break

