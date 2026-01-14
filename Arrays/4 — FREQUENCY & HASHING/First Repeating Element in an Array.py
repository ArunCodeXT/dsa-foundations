arr = [9, 4, 9, 6, 7, 7, 4]
freq={}

for x in arr:
    freq[x]=freq.get(x,0)+1
ans=-1
for x in arr:
    if freq[x]>0:
        ans=x
        break
print(ans)