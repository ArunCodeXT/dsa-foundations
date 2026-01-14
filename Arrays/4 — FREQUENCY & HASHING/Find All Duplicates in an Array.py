arr = [4,3,2,7,8,2,3,1]

duplicates = []
for i in range(len(arr)):
    idx=abs(arr[i])-1

    if arr[idx] < 0:
        duplicates.append(abs(arr[idx]))
    else:
        arr[idx]=-arr[idx]
print(duplicates)



