arr=[1,2,7,6,5,]
k=10
left=0
right=len(arr)-1
found=False
while left < right :
    cur_val=arr[left]+arr[right]
    if cur_val==k :
        found=True
        break
    elif cur_val < k:
        left+=1
    else:
        right-=1
print(found)