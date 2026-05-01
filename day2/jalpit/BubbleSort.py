arr = [5,3,1,4,2]
# Time = O(n^2)
# Space = O(1)

print(arr)
def BubbleSort(arr):
    n = len(arr)
    for i in range(0,n):
        isswap = False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                isswap = True
        if not isswap:  
            break

BubbleSort(arr)
print(arr)