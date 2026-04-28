str='abc'
arr=[1,2,3,4]
num=68

def number(num):
    rev=0
    while(num>0):
        digit=num%10
        rev=rev*10+digit
        num//=10
    return rev


def array(arr):
    start=0
    end=len(arr)-1
    while(start<=end):
        temp=arr[end]
        arr[end]=arr[start]
        arr[start]=temp
        start+=1
        end-=1
    return arr

def string(str):
    return str[::-1]


print(number(num))
print(array(arr))
print(string(str))



