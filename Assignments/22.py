rows = int(input("enter numbers pyramid pattern rows = "))
print("__the pyramid of number pattern__")
for i in range(1,rows + 1):
    for j in range(rows , i,-1):
        print(end ='')
    for k in range(1,i+1):
        print(i,end='')
    print()