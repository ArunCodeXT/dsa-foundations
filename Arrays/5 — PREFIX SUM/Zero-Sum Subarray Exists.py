arr = [4, 2, -3, 1, 6]
prefix_sum=0
seen=set()
found=False
for x in arr:
    prefix_sum+=x

    if prefix_sum==0 or prefix_sum in seen:
        found=True
        break
    seen.add(prefix_sum)
print(found)