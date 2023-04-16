stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}

def displayInventory(stuff):
    lst = list(stuff.keys())
    total = 0
    print('Inventory:')
    for key in lst:
        print(stuff[key], key)
        total += stuff[key]
    print('Total number of items: ', total)


if __name__ == "__main__":
    displayInventory(stuff)
