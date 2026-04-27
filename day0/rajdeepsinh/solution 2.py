for i in range(1,7):
    for j in range(1,7):
        if(i>=2 and i<=5):
            print("*    *",end="")
            break
        else:
            print("*",end="")
    print()
