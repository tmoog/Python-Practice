def calculateTime():
    
    # This first line is provided for you
    monkey_one = input("Is the first monkey smiling?:  ")
    monkey_two = input("Is the second monkey smiling?: ")
    if monkey_one.upper() == "Y" and monkey_two.upper() == "Y":
        print("Uh Oh! We're in trouble!")
    elif monkey_one.upper() == "Y" and monkey_two.upper() == "N":
        print("Yay! We're going to have a good day!")
    elif monkey_one.upper() == "N" and monkey_two.upper() == "Y":
        print("Yay! We're going to have a good day!")
    elif monkey_one.upper() == "N" and monkey_two.upper() == "N":
        print("Uh Oh! We're in trouble!")

    # end assignment


## If you want to test locally run > python monkeyCalculator.py

if __name__ == "__main__":
    calculateTime()
    
