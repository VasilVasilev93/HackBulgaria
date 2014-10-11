def is_an_bn(word):
    end = len(word) - 1
    beg = 0
    count = 0
    n = int(len(word)/2)
    if len(word) % 2 == 1:
        return False
    if word == "":
        return True
    while n > 0:
        if word[beg] == "a" and word[end] == "b":
            count += 1
            end -= 1
            beg += 1
            n -= 1
        else:
            return False
    if count == len(word)/2:
        return True
    return False

print (is_an_bn("bbbaaa"))
