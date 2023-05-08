val = int(input("please enter any value:"))
print("result of a given {0} are :".format(val))
for i in range (1, val + 1):
    if(val%i == 0):
        print("{0}".format(i))