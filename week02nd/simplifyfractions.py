def is_not_prime(n):
    n = abs(n)
    if n == 1:
        return True
    else:
        numOfDiv = 0
        for k in range(1, n + 1):
            if n % k == 0:
                numOfDiv += 1
        if numOfDiv == 2:
            return False
        else:
            return True


def common_divisors(n, m):
    divisors = []
    if n > m:
        for divisor in range(2, n):
            if m % divisor == 0 and n % divisor == 0:
                divisors.append(divisor)
    else:
        for divisor in range(2, m):
            if m % divisor == 0 and n % divisor == 0:
                divisors.append(divisor)
    return divisors


def simplify_fraction(fraction):
    fraction = list(fraction)
    divs = common_divisors(fraction[0], fraction[1])
    if (not is_not_prime(fraction[0])) and not (is_not_prime(fraction[1])):
        return tuple(fraction)
    elif len(divs) > 0:
        for k in divs:
            if fraction[0] % k == 0 and fraction[1] % k == 0:
                fraction[0] //= k
                fraction[1] //= k
            else:
                return tuple(fraction)
    return tuple(fraction)

print (simplify_fraction((4, 10)))
