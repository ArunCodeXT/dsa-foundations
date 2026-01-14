arr = [2, 2, 1, 1, 2, 2, 2]
#Boyer–Moore Voting Algorithm
candidate=None
count=0

for x in arr:
    if count==0:
        candiadte=x
        count=0
    elif candiadte==x:
        count+=1
    else:
        count-=1
print(candiadte)