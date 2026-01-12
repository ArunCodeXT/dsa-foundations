arr = [-1, 0, 1, 2, -1, -4]
k = 0
arr.sort()
n=len(arr)
result=[]

for i in range(n-2):
    if i>0 and arr[i]==arr[i-2]:
        continue
    left=i+1
    right=n-1

    while left < right :
        total=arr[i]+arr[left]+arr[right]

        if total==k :
            result.append((arr[i],arr[left],arr[right]))
            left+=1
            right-=1

            while left < right and arr[left]==arr[left-1]:
                left+=1
            while left < right and arr[right]==arr[right+1]:
                right-=1
        
        elif total < k:
            left+=1
        else:
            right-=1
print(result)
