def member_of_nth_fib_lists(listA, listB, needle):
    first = listA
    second = listB
    nextfib = first + second
    count = 0
    for k in range(0, len(nextfib)):
        if nextfib[k] == needle[k]:
            count += 1
    if count == len(nextfib):
        return True
    return False

print (member_of_nth_fib_lists([7, 11], [2], [7, 11, 2, 2, 7, 11, 2]))
print (member_of_nth_fib_lists([7, 11], [2], [11, 7, 2, 2, 7]))
