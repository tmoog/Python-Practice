def test_range(n):
    try:
        if n in range(0,100):
            print('%s In Range' %str(n))
        else:
            print('%s Out of Range' %str(n))
    except:
        print('Enter a number')

test_range(50)
