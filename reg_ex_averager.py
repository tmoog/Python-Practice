def average_new_revision_lines():
    file_name = input("Enter file: ")
    #file_name = 'mbox-short.txt'
    file = open(file_name)
    import re
    numlist = []
    count = 0
    for line in file:
        x = re.findall('New Revision: ([0-9]+)', line)
        if len(x) > 0:
            count += 1
            num = int(x[0])
            numlist.append(num)
    avg = int(sum(numlist)/ count)
    print(avg)

    
if __name__ == "__main__":
    average_new_revision_lines()
