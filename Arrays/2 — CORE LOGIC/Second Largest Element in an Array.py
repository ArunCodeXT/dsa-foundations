arr=[10,5,20,8]
largest=float('-inf')
second=float('-inf')
for x in arr:
    if x > largest:
        second=largest
        largest=x
    elif x<largest and x>second:
        second=x
if second==float('-inf'):
    print("no second largest")
else:
    print(second)