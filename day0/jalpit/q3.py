n=6
for i in range(0,n+1):
    for j in range(0,n-i):
        print(" ",end="")
    for j in range(0,i):
        print(f" {i}",end="")
    print("")