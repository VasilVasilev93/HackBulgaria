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


def goldbach(n):
    if n <= 2:
        return "Integer must be higher than 2!!!"
    primeaddends = []
    primetuple = []
    for addend1 in range(1, n//2 + 1):
        if is_prime(addend1):
            addend2 = n - addend1
            if is_prime(addend2):
                primetuple.append(addend1)
                primetuple.append(addend2)
                primeaddends.append(tuple(primetuple))
                primetuple = []
    return primeaddends
