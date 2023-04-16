def calculateGrade():
    # Implement your solution in between the two comment blocks
    print("Calculating Grade")
    score = input("Enter score:")
    try:
        score = float(score)
        if score < 0.0 or score > 1.0:
            print('Bad score')
        elif score >= 0.9:
            print('A')
        elif score >= 0.8:
            print('B')
        elif score >= 0.7:
            print('C')
        elif score >= 0.6:
            print ('D')
        else: print('F')
    except:
        print('Bad score')



    # end assignment

## If you want to test locally before you try to sync
## Run > python calculateGrade.py

if __name__ == "__main__":
    calculateGrade()
