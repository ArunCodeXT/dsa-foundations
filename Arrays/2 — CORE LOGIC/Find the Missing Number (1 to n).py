arr = [1, 2, 4, 5]
n=len(arr)
first=n*(n+1)//2
second=0
for i in range(len(arr)):
    second+=arr[i]
missing=first-second
print(missing)


