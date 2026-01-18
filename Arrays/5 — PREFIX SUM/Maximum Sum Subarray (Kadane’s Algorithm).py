arr = [-2,1,-3,4,-1,2,1,-5,4]
max_len=arr[0]
current_len=arr[0]

for i in range(1,len(arr)):
    current_len=max(arr[i],current_len+arr[i])
    max_len=max(current_len,max_len)

print(max_len)