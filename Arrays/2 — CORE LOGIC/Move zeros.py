arr = [0, 1, 0, 3, 12]
n=len(arr)
slow=0
for fast in range(n):
    if arr[fast]!=0:
        arr[slow]=arr[fast]
        slow+=1
for i in range(slow,n):
    arr[i]=0
print(arr)