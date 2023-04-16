def compute_min_and_max() -> None:
    # Write your code below this line.
    numlist=[]
    while True:
        inp = input('Enter a number: ')
        if inp.lower() == 'done':
            break
        try:
            num = float(inp)
        except:
            print('bad data')
        numlist.append(num)
    print('Maximum:', max(numlist))
    print('Minimum:', min(numlist))



if __name__ == "__main__":
    compute_min_and_max()
