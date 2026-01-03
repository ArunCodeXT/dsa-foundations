arr=[10,20,30,40,70]
max_val=arr[0]
for i in range(1,len(arr)):
    if arr[i]>max_val:
        max_val=arr[i]
print(max_val)