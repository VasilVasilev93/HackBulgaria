def sum_of_divisors(n):
    n = abs(n)
    sum = 0
    for k in range(1, n + 1):
        if(n % k == 0):
            sum += k
    return sum
