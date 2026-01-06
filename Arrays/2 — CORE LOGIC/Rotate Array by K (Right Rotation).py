def reverse(arr,start,end):
    while start < end :
        temp=arr[start]
        arr[start]=arr[end]
        arr[end]=temp
        start+=1
        end-=1
arr=[10,20,30,40,50]
n=len(arr)
k=4
k=k%n
reverse(arr,0,n-1)
reverse(arr,0,k-1)
reverse(arr,k,n-1)
print(arr)