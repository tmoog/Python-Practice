def convert_tuples_to_dictionary(tuple):
    dictionary = {}
    for a,b in tuple:
        dictionary[a] = b
    return dictionary

test_tuple = ('a','b'),

print(convert_tuples_to_dictionary(test_tuple))