def string_reverser():
    in_string = input("Enter a string: ")
    n = len(in_string) - 1
    while n >= 0:
        print(in_string[n])
        n = n -1



if __name__ == "__main__":
    string_reverser()
