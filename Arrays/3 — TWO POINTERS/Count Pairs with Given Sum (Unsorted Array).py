arr = [1, 5, 7, -1, 5]
k = 6
freq={}
count=0
for x in arr:
    complement=k-x
    if complement in freq:
        count+=freq[complement]
    freq[x]=freq.get(x,0)+1
print(count)