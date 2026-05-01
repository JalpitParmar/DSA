# Time = O(log n)
# Space = O(1)

# mid = l + (r-l/2) optimization

arr = [1,2,3,4,5]

def BinarySearch(arr,target): 
    l = 0
    r = len(arr)-1
    while l<=r:
        mid = int((l+r)/2)
        if arr[mid]==target: 
            return mid
        if arr[mid]>target:
            r = mid - 1
        if arr[mid]<target:
            l = mid + 1
        if l>r:
            return -1

print(BinarySearch(arr,5))



#recursive binary search

