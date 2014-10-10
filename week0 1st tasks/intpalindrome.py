def is_int_palindrome(n):
    temp = str(n)
    rev = temp[:: -1]
    if temp == rev:
        return True
    else:
        return False
