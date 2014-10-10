from checkprime import is_prime


def prime_factorization(n):
    divs = []
    power = 0
    num = n
    div = 2
    if is_prime(n):
        return "[(%s, 1)] # %s is prime" % (n, n)
    else:
        for i in range(0, n):
            if num % div == 0:
                power += 1
                num //= div
            elif num % div != 0 and power != 0:
                divs.append((div, power))
                div += 1
                power = 0
            else:
                div += 1
    return divs

print (prime_factorization(1000))
