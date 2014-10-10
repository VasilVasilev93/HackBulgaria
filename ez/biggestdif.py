def biggest_difference(arr):
    difference = 0
    num = arr[0]
    for k in range(1, len(arr)):
        if num < arr[k] and abs(difference) < abs(num - arr[k]):
            difference = num - arr[k]
    return difference


print (biggest_difference(range(100)))
