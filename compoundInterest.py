def collect_inputs():
    P = float(input("Principle (amount): "))
    T = float(input("Time: "))
    R = float(input("Rate: "))
    return P, T, R

def SingleCompoundInterest():
    P, T, R = collect_inputs()
    A = P *( 1 + R/100)**T
    CI = round(A - P,2)
    print("Compound Interest: "+str(CI))

def calculateCompoundInterest():
    SingleCompoundInterest()
    print("---")
    SingleCompoundInterest()
    print("---")
    SingleCompoundInterest()
    



    # end assignment

## If you want to test locally run > python compoundInterest.py

if __name__ == "__main__":
    calculateCompoundInterest()
