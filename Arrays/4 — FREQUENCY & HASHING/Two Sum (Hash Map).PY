arr = [2, 7, 11, 15]
k=9
seen={}

for i,x in enumerate(arr):
    complement=k-x

    if complement in seen:
        print((seen[complement],i))
        break
    seen[x]=i