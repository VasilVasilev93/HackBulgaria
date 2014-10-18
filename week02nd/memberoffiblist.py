def member_of_nth_fib_lists(listA, listB, needle):
    first = listA
    second = listB
    nextfib = first + second
    count = 0
    if(needle == first):
        return True
    elif(needle == second):
        return True
    for k in range(0, len(nextfib)):
        if k >= len(needle):
            break
        if nextfib[k] == needle[k]:
            count += 1
    if count == len(nextfib):
        return True
    return False

print (member_of_nth_fib_lists([1, 2], [1, 3], []))
