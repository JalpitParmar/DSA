# Time = O(n)
# Space = O(1)

arr = [1,2,3,5]

def LinearSearch(arr,target):
    for i in range(0,len(arr)-1):
        if target==arr[i]:
            return i
    return -1

print(LinearSearch(arr,2))