arr1 = [1, 2, 3, 4]
arr2 = [3, 4, 5, 6]
seen=set()
for x in arr1:
    seen.add(x)
for x in arr2:
    seen.add(x)
union=list(seen)
print(union)