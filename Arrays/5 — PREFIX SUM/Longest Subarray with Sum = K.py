arr = [1, -1, 5, -2, 3]
k = 3
index={0:-1}
max_len=0
prefix_sum=0

for i,x in enumerate(arr):
    prefix_sum+=x

    if prefix_sum-k in index:
        max_len=max(max_len,i-index[prefix_sum-k])
    if prefix_sum not in index:
        index[prefix_sum]=i
print(max_len)
