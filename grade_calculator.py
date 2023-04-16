print('Calculating Grade')
def collect_and_prep_score():
    try:
        score = float(input('Enter score: '))
    except:
        score = -1
        print('Bad score')
    
    return score

def compute_grade(score):
    if score > 1:
        print('Bad score')
    elif score >= 0.9:
        print('A')
    elif score >= 0.8:
        print('B')
    elif score >= 0.7:
        print('C')
    elif score >= 0.6:
        print('D')
    elif score >= 0:
        print('F')
    else:
        print('Bad score')



if __name__ == "__main__":
    score = collect_and_prep_score()
    compute_grade(score)
