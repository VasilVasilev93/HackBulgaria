def contains_digit(number, digit):
    temp = str(number)
    for k in range(0, len(temp)):
        if number % 10 == digit:
            return True
        else:
            return False
    return False
