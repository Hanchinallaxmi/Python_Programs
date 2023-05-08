names=['a','b','c']
grades=[1,2,3,4,5,6]



#1st code
fd=open(r"a.txt","w")
for i in range(5):
    record=names[i] +str(" ")+str(grades[i])+str("\n")
    val=fd.write(record)
fd.close()

#2nd code
fd=open(r"a.txt","r")
file_data=fd.readlines()
print(file_data[-1])
fd.close()



print("value:%5.2i"%(1,05.333))
print("total students:%3d,boys:%2d"%(240,120))
print("%7.30"%(25))
print("%10.3e"%(356.08977))