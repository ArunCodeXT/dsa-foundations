arr = [1, 3, 4, 7, 10]
k = 15
left=0
right=len(arr)-1
min_dif=float('inf')
best_pair=None
while left < right:
    curr=arr[left]+arr[right]
    diff=abs(k-curr)

    if diff < min_dif:
        min_dif=diff
        best_pair=(arr[left],arr[right])

    elif curr < k:
        left+=1
    elif curr > k:
        right-=1
    else:
        break
print(best_pair)

