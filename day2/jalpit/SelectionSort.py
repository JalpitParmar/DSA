arr = [5,3,1,4,2]
n = len(arr)

# Time = O(n)
# Space = O(1)

for i in range(0,n):
    min = i
    for j in range(i,n):
        if arr[min]>arr[j]:
            min=j
    arr[min],arr[i]=arr[i],arr[min]

print(arr)