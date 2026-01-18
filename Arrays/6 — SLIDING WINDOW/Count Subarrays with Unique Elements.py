arr = [1, 2, 3]
count=0
freq={}
left=0

for right in range(len(arr)):
    freq[arr[right]]=freq.get(arr[right],0)+1

    while freq[arr[right]] > 1:
        freq[arr[left]]-=1
        left+=1
    count+=(right-left+1)
print(count)


