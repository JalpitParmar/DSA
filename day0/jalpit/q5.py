n=10

for i in range(0,n+1):
    for j in range(0,n-i):
        print(" ",end="")
    for j in range(0,i):
        print(" *",end="")
    print("")

for i in range(n,0,-1):
    for j in range(0,n-i):
        print(" ",end="")
    for j in range(0,i):
        print(" *",end="")
    print("")