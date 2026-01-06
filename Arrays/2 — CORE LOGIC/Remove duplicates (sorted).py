arr = [1, 1, 2, 2, 3]
n=len(arr)
slow=0
for fast in range(1,n):
    if arr[fast]!=arr[slow]:
        slow+=1
        arr[slow]=arr[fast]
print("lenth=",slow+1)
print("array=",arr[:slow+1])             