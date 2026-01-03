arr=[10,20,30,40,50]
n=len(arr)
last=arr[n-1]
for i in range(n-1,0,-1):
    arr[i]=arr[i-1]
arr[0]=last
print(arr)