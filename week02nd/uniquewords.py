def unique_words_count(arr):
    count = 0
    word = arr[0]
    if len(arr) > 0:
        count += 1
    for k in arr:
        if word != k:
            count += 1
    return count

print unique_words_count(["python", "python", "python", "ruby"])
