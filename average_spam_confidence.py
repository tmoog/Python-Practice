def print_count_of_spam_confidence() -> None:
    # Write your code below this line
    fname = input("Enter a file name: ")
    fhand = open(fname)
    count = 0
    total = 0
    for line in fhand:
        if line.startswith('X-DSPAM-Confidence:'):
            count = count + 1
            colpos = line.find(':')
            num = float(line[colpos+2:])
            total = total + num
    print('Average spam confidence:', total/count)


if __name__ == "__main__":
    print_count_of_spam_confidence()
    
