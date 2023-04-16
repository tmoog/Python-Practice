def print_file_as_uppercase() -> None:
    # Write your code below this line
    fname = input("Enter a file name: ")
    fhand = open(fname)
    for line in fhand:
        line = line.rstrip()
        line = line.upper()
        print(line)



if __name__ == "__main__":
    print_file_as_uppercase()
