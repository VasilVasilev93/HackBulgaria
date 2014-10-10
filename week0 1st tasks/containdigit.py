def contains_digit(number, digit):
    temp = str(number)
    for k in range(0, len(temp)):
        if number % 10 == digit:
            return True
        number //= 10
    return False

print ((contains_digit(1234567, 9)))
