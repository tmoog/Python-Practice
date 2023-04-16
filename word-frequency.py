def word_frequency(fname, n):
    fhand = open(fname)
    count = 0
    for line in fhand:
        if line.find(n) == -1:
            continue
        else:
            count = count+1
            
    print(n, 'was found', count, 'times')

word_frequency('hello.txt', 'you')