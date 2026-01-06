arr = [1, 2, 4, 6, 8, 9]
k = 10

left = 0
right = len(arr) - 1

found = False

while left < right:
    curr_sum = arr[left] + arr[right]

    if curr_sum == k:
        found = True
        break
    elif curr_sum < k:
        left += 1
    else:
        right -= 1

print(found)
