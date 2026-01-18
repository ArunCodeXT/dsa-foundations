arr = [1, 2, 3]
k = 5
left=0
window=0
count=0

for right in range(len(arr)):
    window+=arr[right]

    while (right-left+1) >=k:
        window-=arr[left]
        left+=1
    count+=(right-left+1)
print(count)