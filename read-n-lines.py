def read_last_n_lines(n):
    fname = input('Enter a flie name: ')
    fhand = open(fname)
    data = fhand.readlines()
    print(data[n:])
        

read_last_n_lines(1)

