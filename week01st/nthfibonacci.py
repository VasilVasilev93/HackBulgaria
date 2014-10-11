def nth_fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        first = 1
        second = 1
        for k in range(0, n - 2):
            next = first + second
            first = second
            second = next
        return next

print (nth_fibonacci(10))
