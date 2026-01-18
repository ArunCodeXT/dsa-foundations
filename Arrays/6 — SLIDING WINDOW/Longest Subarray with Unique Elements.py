arr = [1, 2, 3, 1, 2, 3, 4, 5]
left=0
freq={}
max_len=0

for right in range(len(arr)):
    freq[arr[right]]=freq.get(arr[right],0)+1

    while freq[arr[right]]>1:
        freq[arr[left]]-=1
        left+=1
    
    max_len=max(max_len,right-left+1)
print(max_len)