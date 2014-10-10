def prepare_meal(number):
    spam = ""
    count = 0
    for k in range(1, number):
        if (3**k > number):
            break
        if number % 3 ** k == 0:
            count += 1
    if count > 0:
        for i in range(0, count):
            spam += "spam "
    if number % 5 == 0 and count != 0:
        spam += "and eggs"
    elif number % 5 == 0 and count == 0:
        spam += "eggs"
    return spam

print prepare_meal(45)
