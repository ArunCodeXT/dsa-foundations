arr = [1, 3, 4, 2, 2]
duplicate=-1
for i in range(len(arr)):
    idx=abs(arr[i])
    if arr[idx]<0:
        duplicate=idx
        break
    else:
        arr[idx]=-arr[idx]
print(duplicate)
