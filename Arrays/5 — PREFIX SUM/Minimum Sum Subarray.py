arr =  [3, -4, 2, -3, -1, 7, -5]
min_len=arr[0]
current_len=arr[0]

for i in range(1,len(arr)):
    current_len=min(arr[i],current_len+arr[i])
    min_len=min(current_len,min_len)

print(min_len)