def max_min_dict():
    max=None
    min=None
    d={'a':1, 'b':2, 'c':3, 'd':4}
    for key in d:
        if max == None:
            max = d[key]
            min = d[key]
        elif d[key] > max:
            max = d[key]
        elif d[key] < min:
            min = d[key]
    print('Max:', max, 'Min:', min)

max_min_dict()
