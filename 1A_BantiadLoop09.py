for i in range(1, 11):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                print(i)
                break
    else:
        print(i)