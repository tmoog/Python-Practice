def count_lines(fname):
    fhand = open(fname)
    count = 0
    for line in fhand:
        count = count + 1
    print('Line Count:', count)

count_lines('hello.txt')