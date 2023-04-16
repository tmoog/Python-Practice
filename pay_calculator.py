# Logic to "wrap" in functions
def find_pay_from_hours_and_rate(hrs, rate):
    overtime = hrs - 40
    if overtime > 0:
        total_pay = (40 * rate) + (overtime * rate * 1.5)
    else:
        total_pay = (hrs * rate)
    print('Pay:', total_pay)

    return f"Pay: {total_pay}"

def compute_pay() :
    try:
        hrs = float(input("Enter Hours: "))
        rate = float(input("Enter Rate: "))
    except:
        print ('Error, please enter numeric input')
        exit()
    
    return find_pay_from_hours_and_rate(hrs, rate)
 
if __name__ == "__main__":
    compute_pay()
