def fibonacci_num(m):
    if m < 0:
        print("incorrect input ")
    elif m == 0:
        return 0
    elif m == 1 or m ==2:
        return 1
    else:
        return fibonacci_num(m-1)+fibonacci_num(m-2)
        return v
    print(fibonacci_num(2))