arr = [1, 2, 3]
k = 3
count=0
for i in range(len(arr)):
    current_sum=0
    for j in range(i,len(arr)):
        current_sum+=arr[j]
        if current_sum==k:
            count+=1
print(count)