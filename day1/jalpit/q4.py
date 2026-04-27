arr=[65,98,15,32]

largest=0
second_largest=0
for i in arr:
    if i>largest:
        second_largest=largest
        largest=i
print("Largest:",largest)
print("Second Largest:",second_largest)