def swap(str1, str2):
    nstr1 = str2[:2] + str1[2:]
    nstr2 = str1[:2] + str2[2:]
    nstr = nstr1 + ' ' + nstr2
    return nstr

print(swap('abc', 'xyz'))
