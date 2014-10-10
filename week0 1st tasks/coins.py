def calculate_coins(sum1):
    sum1 = int(sum1 * 100)
    dic = {
        "100": 0,
        "50": 0,
        "20": 0,
        "10": 0,
        "5": 0,
        "2": 0,
        "1": 0
    }
    stinki = ["100", "50", "20", "10", "5", "2", "1"]
    for k in stinki:
        while sum1 >= int(k):
            if sum1 == 0:
                break
            if sum1 - int(k) >= 0:
                sum1 -= int(k)
                dic[k] += 1
    return dic

print (calculate_coins(2.85))
