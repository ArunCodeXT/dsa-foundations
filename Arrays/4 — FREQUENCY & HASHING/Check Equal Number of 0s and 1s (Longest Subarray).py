arr = [0, 1, 0, 1, 1, 1, 0]
prefix_sum=0
freq={0:-1}
max_len=0

for i in range(len(arr)):
    if arr[i]==0:
        prefix_sum-=1
    else:
        prefix_sum+=1

    if prefix_sum in freq:
        max_len=max(max_len,i-freq[prefix_sum])
    else:
        freq[prefix_sum]=i
print(max_len)