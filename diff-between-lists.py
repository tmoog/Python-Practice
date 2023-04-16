def diff_bw_lists(t, t2):
    diff = []
    for n in t:
        if n not in t2:
            diff.append(n)
    for x in t2:
        if x not in t:
            diff.append(x)
    print(diff)

t = [1,3,5,7,9]
t2 = [1,2,4,6,7,8]
diff_bw_lists(t, t2)
