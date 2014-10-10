def count_words(arr):
    word = ""
    words = {}
    count = 0
    for k in arr:
        word = k
        for i in arr:
            if word == i:
                count += 1
        words[word] = count
        count = 0
    return words

print (count_words(["python", "python", "python", "ruby"]))
