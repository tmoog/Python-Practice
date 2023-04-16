def averages():
    # Write code below this line, remember that lines in a functions are indented!
    count = 0
    total = 0
    min = None
    max = None
    while True:
        try:
            num = input('Enter a number: ')
            num = int(num)
            count = count + 1
            total = num + total
            if min == None:
                min = num
            elif num < min:
                min = num
            if max == None:
                max = num
            elif num > max:
                max = num
        except:
            if num == 'done':
                break
            else:
                print('bad data')
    print(total, count, max, min)




    
    #Note: the end should look something like this:
    #print(total, count, max, min)

    
## if you want to test locally before you try to sync run > python averages.py
if __name__ == "__main__":
    averages() # Here is where your averages function is being called when we run python averages.py!
    
