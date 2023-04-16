def countDayOfTheWeek():
    # This first line is provided for you
    file_name = input("Enter a file name: ")
    fhand = open(file_name)
    d = dict()
    for line in fhand:
        line = line.rstrip()
        words = line.split()
        if line.startswith('From'):
            if line.startswith('From:'):
                continue
            else:
                day = words[2]
                if day not in d:
                    d[day] = 1
                else:
                    d[day] += 1
    print(d)







## if you want to test locally run > python payCalculator.py
if __name__ == "__main__":
    countDayOfTheWeek()
