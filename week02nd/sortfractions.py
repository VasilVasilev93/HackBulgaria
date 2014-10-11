from simplifyfractions import simplify_fraction


def sort_fraction_list(fraction):
    for i in range(0, len(fraction) - 1):
        for k in range(0, len(fraction) - 1):
            if (fraction[k][0] / fraction[k][1] >
                    fraction[k + 1][0] / fraction[k + 1][1]):
                temp = fraction[k]
                fraction[k] = fraction[k+1]
                fraction[k+1] = temp
    return fraction


def sort_fractions(fractions):
    n = []
    for i in range(0, len(fractions)):
        n.append(simplify_fraction(fractions[i]))
    return sort_fraction_list(n)
print (sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]))
