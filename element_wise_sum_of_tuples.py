def compute_element_wise_sum_of_tuples(a, b, c):
    result = tuple(map(sum, zip(a,b,c)))
    print(result)

a = (1,2,3,4)
b = (3,5,2,1)
c = (2,2,3,1)

compute_element_wise_sum_of_tuples(a, b, c)

