arr=[1,3,6,7,8,10,13,20]
even=0
odd=0
for i in range(len(arr)):
    if arr[i]%2==0:
        even+=1
    else:
        odd+=1
print("Even =",even)
print("odd=",odd)