n=6
for i in range(0,n+1):
    x = 0
    if i%2:
        x=1
    else: 
        x=0
    for j in range(0,i):
        if x==1:
            print(x,end="")
            x=0
        else:
            print(x,end="")
            x=1
    print("")