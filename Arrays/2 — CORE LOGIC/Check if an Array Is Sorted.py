arr=[10,30,80,50,60]
n=len(arr)
is_sorted=True
for i in range(n-1):
    if arr[i]>arr[i+1]:
        is_sorted=False
        break
print(is_sorted)