arr = [2, 3, 1, 2, 4, 3]
k=7
min_len=float('inf')
left=0
current=0

for right in range(len(arr)):
    current+=arr[right]

    while current >= k:
        min_len=min(min_len,right-left+1)
        current-=arr[left]
        left+=1

print(0 if min_len==float('inf') else min_len)

