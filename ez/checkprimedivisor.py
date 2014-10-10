from checkprime import is_prime


def prime_number_of_divisors(n):
    n = abs(n)
    num = 0
    for k in range(1, n + 1):
        if(n % k == 0):
            num += 1
    return (is_prime(num))
print (prime_number_of_divisors(7))
