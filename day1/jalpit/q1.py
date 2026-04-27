n=688
arr=[1,2,3,4] 
str="abc"

def rev_number(n):
    ans_n=0
    while n != 0:
        x = n%10
        ans_n = ans_n * 10 + x
        n //= 10
    return ans_n

def rev_arr(arr):
    l=0
    r=len(arr)-1
    while l<=r:
        tamp = arr[r]
        arr[r]= arr[l]
        arr[l]= tamp
        r-=1
        l+=1 
    return arr

def rev_str(str):
    return str[::-1]

print("before")
print(n)
print(arr)
print(str)
print("===========")

print("after")
print(rev_number(n))
print(rev_arr(arr))
print(rev_str(str))
print("===========")


