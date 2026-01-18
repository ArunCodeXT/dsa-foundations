arr = [1, 12, -5, -6, 50, 3]
k = 4
window=sum(arr[:k])
max_sum=window

for i in range(k,len(arr)):
    window+=arr[i]
    window-=arr[i-k]
    max_sum=max(max_sum,window)
max_avg=max_sum/k
print(max_avg)