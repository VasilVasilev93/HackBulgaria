def unique_words_count(arr):
    count = 0
    if len(arr) > 0:
        count += 1
        word = arr[0]
    else:
        return count
    for k in arr:
        if word != k:
            count += 1
            word = k
    return count

print (unique_words_count([]))
