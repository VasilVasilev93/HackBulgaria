def is_number_balanced(n):
    temp = str(n)
    left = 0
    right = 0
    for k in range(0, len(temp)):
        if k >= len(temp) / 2:
            left += n % 10
        else:
            right += n % 10
        n //= 10
    if left == right:
        return True
    return False
