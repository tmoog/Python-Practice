def mailbox_counter() -> None:
    file_name = input("Enter a file name: ")
    fhand = open(file_name)
    count = 0
    for line in fhand:
        if line.startswith('From'):
            if line.startswith('From:'):
                continue
            count = count + 1
            words = line.split()
            print(words[1])
    print('There were', count, 'lines in the file with From as the first word')


    
if __name__ == "__main__":
    mailbox_counter()
