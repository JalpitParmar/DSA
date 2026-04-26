for i in range(1,12):
    print(" "*(12-i),end="")
    for j in range(1,i+1):
        if(i%2!=0):
            print("* ",end="")
    print()
print()

for i in range(10,1,-1):
    print(" "*(13-i),end="")
    for j in range(1,i):
        if(i%2==0):
            print("* ",end="")
    print()
