def factorial(num):
    if num == 1:
        return num
    else:
        return num*factorial(num-1)
    num=int(input("enter a number:"))
    if num<0:
        print("factorial cannot be found for negative numbers")
    elif num==0:
        print("factorial of 0 is 1")
    else:
        print("factorial of",num,"is:",factorial(num))
    