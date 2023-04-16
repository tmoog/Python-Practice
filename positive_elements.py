def print_positive_tuple_elements() -> None:
    input_tuples = (input("Enter a list of tuples "))
    #input_tuples = '[(-4, 5, 9), (-3, 2, 3), (-3, 5, 6), (4, -6)]'
    #print(input_tuples)
    list_of_tuples = eval(input_tuples)
    positive_tuples = []

    for item in list_of_tuples:
        itemHasANegative = False
        for element in item:
            if element <= 0:
                itemHasANegative = True
        if (not itemHasANegative):
            positive_tuples.append(item)
    print(positive_tuples)
    
    

    
if __name__ == "__main__":
    print_positive_tuple_elements()
