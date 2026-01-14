arr = [100, 4, 200, 1, 3, 2]
seen={}
longest=0
for x in arr:
    if x-1 not in seen:
        current=x
        count=1

        while current+1 in arr:
            current+=1
            count+=1
        longest=max(longest,count)
print(longest)
        
        
