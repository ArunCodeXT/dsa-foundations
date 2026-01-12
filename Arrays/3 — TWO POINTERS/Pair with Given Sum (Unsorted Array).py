arr = [8, 5, 1, 6, 7]
k=10
seen=set()
found=False
for x in arr:
    if k-x in seen:
        found=True
        break
    seen.add(x)
print(found)