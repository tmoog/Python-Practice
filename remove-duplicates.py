def remove_duplicates(t):
    t2 = []
    for n in t:
        if n not in t2:
            t2.append(n)
    print(t2)

t = ['hi', 'hello', 'hey', 'hi']
remove_duplicates(t)