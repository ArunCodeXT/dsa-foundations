arr = [1, 1, 1]
k = 2
freq={0:1}
prefix_sum=0
count=0

for i,x in enumerate(arr):
    prefix_sum+=x

    if prefix_sum-k in freq:
        count+=freq[prefix_sum-k]
    freq[prefix_sum]=freq.get(prefix_sum,0)+1
print(count)