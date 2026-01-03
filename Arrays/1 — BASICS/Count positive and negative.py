arr=[1,3,-6,-7,8,-10,13,20]
positive=0
negative=0
for i in range(len(arr)):
    if arr[i]>0:
        positive+=1
    elif arr[i]<0:
        negative+=1
print("negative =",negative)
print("positive =",positive)