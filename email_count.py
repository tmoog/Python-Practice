def print_most_emails() -> None:
    file_name = input("Enter a file name: ")
    fhand = open(file_name)
    dict={}
    #Read and parse the “From” lines and pull out the addresses from the line.
    for line in fhand:
        if line.startswith('From'):
            if line.startswith('From:'):
                continue
            else:
                words=line.split()
                sender=words[1]
            #Count the number of messages from each person using a dictionary.
                dict[sender] = dict.get(sender, 0)+1
            #After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary.
                lst=[]
                for key, value in dict.items():
                    tup=(value, key)
                    lst.append(tup)
                #Sort the list in reverse order and print out the person who has the most commits.
                    lst = sorted(lst, reverse=True)
    for value,key in lst[:1]:
        print(key, value)



if __name__ == "__main__":
    print_most_emails()
    
