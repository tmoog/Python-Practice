def check_if_element_in_tuple_of_tuples(item, tuple_of_tuples): 
    item_lower = item.lower
    item_present = False
    for tuples in tuple_of_tuples:
        for element in tuples:
            if element.lower == item_lower:
                item_present = True
    print('Check if', item,'present in said tuple of tuples!')
    print(item_present)

item = 'Olive'
tuple_of_tuples = [('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime')]

check_if_element_in_tuple_of_tuples(item, tuple_of_tuples)


    
