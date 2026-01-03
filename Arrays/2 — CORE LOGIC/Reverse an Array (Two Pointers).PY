arr=[10,20,30,40,50]
left=0
right=len(arr)-1

while left < right:
    temp=arr[left]
    arr[left]=arr[right]
    arr[right]=temp
    left+=1
    right-=1

print(arr)
