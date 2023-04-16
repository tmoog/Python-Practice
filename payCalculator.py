def calculatePay():
    # This first line is provided for you
    hrs = input("Enter Hours:")
    rate = input("Enter Rate:")
    try:
        hrs = float(hrs)
    except:
        print('Error, please enter numeric input')
    try:
        rate = float(rate)
    except:
        print('Error, please enter numeric input')
    if (hrs) <= 40:
        pay = rate * hrs
    elif hrs > 40:
        ot = hrs - 40
        pay = (40 * rate) + (ot * rate * 1.5)
    print('Pay:', pay)

    
    # end assignment

## if you want to test locally before you try to sync
## run > python payCalculator.py

#Ignore this for now. 
if __name__ == "__main__":
    calculatePay()
