arr1 = [1, 2, 2, 1]
arr2 = [2, 2]
seen=set(arr1)
result=set()
for x in arr2:
    if x in seen:
            result.add(x)
print(list(result))
