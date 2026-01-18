from collections import deque
arr = [12, -1, -7, 8, -15, 30, 16, 28]
k = 3
q=deque()
result=[]

for i in range(len(arr)):

    if arr[i]<0:
        q.append(i)

    if i >=k:
        while q and q[0]<i-k+1:
            q.popleft()
        if q:
            result.append(arr[q[0]])
        else:
            result.append(0)
print(result)