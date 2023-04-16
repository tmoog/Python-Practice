def count_strings(t):
    count = 0
    for n in t:
        if len(n) >= 2 and n[0] == n[-1]:
            count = count + 1
    print(count)

t = ['abc', 'xyz', 'aba', '1221']
count_strings(t)