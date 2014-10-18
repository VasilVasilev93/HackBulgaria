def nth_fib_lists(listA, listB, n):
    if n == 1:
        return listA
    elif n == 2:
        return listB
    else:
        first = listA
        second = listB
        for k in range(0, n - 2):
            nextfib = first + second
            first = second
            second = nextfib
        return nextfib