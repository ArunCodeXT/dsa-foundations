arr = [2, 4, 6, 8, 10]
ps=[0]*len(arr)
ps[0] = arr[0]

for i in range(1,len(arr)):
    ps[i]=ps[i-1]+arr[i]

l=1
r=3

if l==0:
    print(ps[r])
else:
    print(ps[r]-ps[l-1])