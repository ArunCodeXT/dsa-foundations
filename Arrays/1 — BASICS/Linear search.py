arr=[10,20,30,60,80,40]
x=30
index=-1
for i in range(len(arr)):
    if arr[i]==x:
        index=i
        break
print(index)
