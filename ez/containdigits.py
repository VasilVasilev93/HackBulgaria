from containdigit import contains_digit


def contains_digits(number, digits):
    count = 0
    for k in digits:
        if contains_digit(number, k):
            count += 1
    if count == len(digits):
        return True
    else:
        return False
print (contains_digits(402123, [0, 3, 4]))
