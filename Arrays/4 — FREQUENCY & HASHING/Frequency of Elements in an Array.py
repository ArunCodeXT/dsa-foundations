arr = [1, 2, 2, 3, 1, 4]
freq={}
for x in arr:
    freq[x]=freq.get(x,0)+1

for key,value in freq.items():
    print(key,"->",value)