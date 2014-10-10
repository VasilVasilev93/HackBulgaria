
def what_is_my_sign(day, month):
    signs = [
        [20, "Capricorn"],
        [19, "Aquarius"],
        [20, "Pisces"],
        [20, "Aries"],
        [21, "Taurus"],
        [21, "Gemini"],
        [22, "Cancer"],
        [22, "Leo"],
        [23, "Virgo"],
        [22, "Libra"],
        [21, "Scorpio"],
        [20, "Sagittarius"]
    ]
    if day <= signs[month - 1][0]:
        return signs[month - 1][1]
    else:
        return signs[month][1]

print (what_is_my_sign(9, 1))
