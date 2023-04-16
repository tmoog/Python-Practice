def calculateAbsolute():
    in_num  = int(input("Enter a number: "))
    if in_num > 21:
        result = (in_num - 21)*2
    else:
        result = 21-in_num
    print('Result:', result)

## If you want to test locally run > python payCalculator.py

if __name__ == "__main__":
    calculateAbsolute()
