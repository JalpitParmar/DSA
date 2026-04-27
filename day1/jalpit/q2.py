n=688
arr=[1,2,3,4] 
str="aba"

def number_Palindrome(n):
    ans_n=0
    while n != 0:
        x = n%10
        ans_n = ans_n * 10 + x
        n //= 10
        
    return n==ans_n

def arr_Palindrome(arr):
    tamp_x= arr.copy()
    l=0
    r=len(arr)-1
    while l<=r:
        tamp = arr[r]
        arr[r]= arr[l]
        arr[l]= tamp
        r-=1
        l+=1 
    return tamp_x==arr

def str_Palindrome(str):
    return str==str[::-1]



print("Palindrome")
print(n," ",number_Palindrome(n))
print(arr," ",arr_Palindrome(arr))
print(str," ",str_Palindrome(str))



