import re

def count_pattern_in_file():
    regular_expression = input("Enter a regular expression: ")
    #regular_expression = '^Author'
    file_name = 'mbox-long.txt'
    file = open(file_name)
    import re
    count = 0
    for line in file:
        if re.search(regular_expression, line):
            count += 1
    print('mbox.txt had', count, 'lines that matched', regular_expression)


    
if __name__ == '__main__':
    count_pattern_in_file()
