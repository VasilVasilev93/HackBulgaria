def is_prime(n):
    n = abs(n)
    if n == 1:
        return False
    else:
        numOfDiv = 0
        for k in range(1, n + 1):
            if n % k == 0:
                numOfDiv += 1
        if numOfDiv == 2:
            return True
        else:
            return False
