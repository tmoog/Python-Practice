def original_sorted_word_printer() -> None:    
    file_name = input("Enter file: ")
    fhand = open(file_name)
    words_list = []
    for line in fhand:
        words = line.split()
        for word in words:
            if word not in words_list:
                words_list.append(word)
    words_list.sort()
    print(words_list)




if __name__ == "__main__":
    original_sorted_word_printer()
