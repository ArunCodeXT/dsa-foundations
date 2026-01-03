arr=[10,2,80,5,70]
smallest=float('inf')
second=float('inf')
for x in arr:
    if x < smallest:
        second=smallest
        smallest=x
    elif x > smallest and x < second :
        second=x
if second==float('-inf'):
    print("no second smallest")
else:
    print(second)        