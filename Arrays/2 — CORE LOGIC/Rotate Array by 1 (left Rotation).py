arr=[10,20,30,40,50]
n=len(arr)
first=arr[0]
for i in range(n-1):
    arr[i]=arr[i+1]
arr[n-1]=first
print(arr)