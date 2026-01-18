arr = [5, -3, 5]
max_sum=current_max=arr[0]
min_sum=current_min=arr[0]
total=0

for i in range(len(arr)):
    total+=arr[i]
    if i>0:
        current_max=max(arr[i],current_max+arr[i])
        max_sum=max(max_sum,current_max)

        current_min=min(arr[i],current_min+arr[i])
        min_sum=min(current_min,min_sum)

if max_sum < 0:
    print(max_sum)
else:
    print(max(max_sum, total - min_sum))
