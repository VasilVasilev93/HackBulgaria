from intpalindrome import is_int_palindrome


def next_hack(n):
    n += 1
    num = "{0:b}".format(n)
    count = 0
    for k in num:
        if k == "1":
            count += 1

    if count % 2 == 1 and is_int_palindrome(num):
        print "asd"
        return n
    return next_hack(n)

print (next_hack(8031))
