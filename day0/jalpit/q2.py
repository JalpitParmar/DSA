n = 6 
for i in range(0,n+1):
    for j in range(0,n):
        if i==0 or i==n:
            print("*",end="")
        else:
            print("*    *",end="")
            break
    print("")