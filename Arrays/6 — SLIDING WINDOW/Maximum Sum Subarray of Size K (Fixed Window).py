arr = [2, 1, 5, 1, 3, 2]
k = 3
window=sum(arr[:k])
max_sum=window

for i in range(k,len(arr)):
    window+=arr[i]
    window-=arr[i-k]
    max_sum=max(max_sum,window)
print(max_sum)
