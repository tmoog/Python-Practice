def get_words_list():
    words = []
    while True:
        inp = input('Enter word: ')
        if inp.upper() == 'DONE':
            break
        else:
            words.append(inp)
    return words

def longest_word():
    longest = 0
    words = get_words_list()
    for n in words:
        if len(n) > longest:
            longest = len(n)
            longest_word = n
    print('Longest word:', longest_word)
    print('Length of longest word:', longest)

longest_word()
        
