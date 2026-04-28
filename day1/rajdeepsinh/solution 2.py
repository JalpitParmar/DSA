number=68
arr=[1,2,3,4]
str='abc'

def rev(num):
    rev=0
    while(num>0):
        digit=num%10
        rev=rev*10+digit
        num//=10
    return rev

rev=rev(number)
if(number==rev):
    print("number is palindrome")
else:
    print("number is not palindrome")


def array(arr):
    tamp_x= arr.copy()
    start=0
    end=len(arr)-1
    while(start<=end):
        temp=tamp_x[start]
        tamp_x[start]=tamp_x[end]
        tamp_x[end]=temp
        start+=1
        end-=1
    return tamp_x

arr2=array(arr)
if(arr==arr2):
    print("array is palindrome")
else:
    print("array is not palindrome")

def string(str):
    return str[::-1]

str2=string(str)
if(str==str2):
    print("strings is palindrome")
else:
    print("strings is not palindrome")
