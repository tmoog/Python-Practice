def sort_tuple_by_float(tuple):
    for a,b in tuple:
        a,b = b,a
    
    tuple.sort(reverse=True)

    for a,b in tuple:
        a,b = b,a
    
    print(tuple)

tuple=[('item1','12.20'), ('item2','15.10'), ('item3', '24.5')]

sort_tuple_by_float(tuple)
