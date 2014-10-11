def nth_fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        first = 1
        second = 1
        for k in range(2, n):
            next = first + second
            first = second
            second = next
        return next


def sum_of_digits(n):
    n = abs(n)
    temp = str(n)
    result = 0
    for k in range(0, len(temp)):
        result += n % 10
        n /= 10
    return result


def sum_of_digits1(n):
    temp = str(n)
    result = 0
    for k in range(0, len(temp)):
        result += n % 10
        n /= 10
    return result


def sum_of_divisors(n):
    n = abs(n)
    sum = 0
    for k in range(1, n + 1):
        if(n % k == 0):
            sum += k
    return sum


def is_prime(n):
    n = abs(n)
    if n == 1:
        return False
    else:
        numOfDiv = 0
        for k in range(1, n + 1):
            if n % k == 0:
                numOfDiv += 1
        if numOfDiv == 2:
            return True
        else:
            return False


def prime_number_of_divisors(n):
    n = abs(n)
    num = 0
    for k in range(1, n + 1):
        if(n % k == 0):
            num += 1
    return (is_prime(num))


def sevens_in_a_row(arr, n):
    count = 0
    for item in arr:
        if item == 7:
            count += 1
        else:
            count = 0
        if count == n:
            return True
    return False


def is_int_palindrome(n):
    temp = str(n)
    rev = temp[:: -1]
    if temp == rev:
        return True
    else:
        return False


def contains_digit(number, digit):
    temp = str(number)
    for k in range(0, len(temp)):
        if number % 10 == digit:
            return True
        number /= 10
    return False


def contains_digits(number, digits):
    count = 0
    for k in digits:
        if contains_digit(number, k):
            count += 1
    if count == len(digits):
        return True
    else:
        return False


def is_number_balanced(n):
    temp = str(n)
    left = 0
    right = 0
    for k in range(0, len(temp)):
        if k >= len(temp) / 2:
            left += n % 10
        else:
            right += n % 10
        n /= 10
    if left == right:
        return True
    return False


# errors
def count_substrings(haystack, needle):
    stack = ""
    count = 0
    for k in range(0, len(haystack)):
        stack += haystack[k]
        if len(stack) == len(needle):
            if stack == needle:
                count += 1
                stack = haystack[k]
            else:
                stack = haystack[k]
    return count


def count_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    count = 0
    for k in str:
        if k in vowels:
            count += 1
    return count


def count_consonants(str):
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k',
                  'l', 'm', 'n', 'p', 'q', 'r', 's', 't',
                  'v', 'w', 'x', 'z']
    count = 0
    for k in str:
        if k in consonants:
            count += 1
    return count


def number_to_list(n):
    num = str(n)
    l = []
    for k in range(1, len(num) + 1):
        l.append(k)
    return l


def list_to_number(digits):
    num = ""
    for k in digits:
        num += str(k)
    return num

# print nth_fibonacci(4)
# print sum_of_digits(123)
# print sum_of_divisors(8)
# print is_prime(2)
# print prime_number_of_divisors(8)
# print sevens_in_a_row([1, 2, 7, 7, 7, 3, 4], 3)
# print is_int_palindrome(4224)
# print is_int_palindrome(4223)
# print contains_digit(123, 4)
# print contains_digit(123, 3)
# print contains_digits(12344, [1, 3, 4])
# print is_number_balanced(521260)
# print count_substrings("babababa", "baba")
# print count_vowels("Github is the second best thing that happend to"
#                   "programmers, after the keyboard!")
#print count_consonants("Github is the second best thing that"
#                       " happend to programmers, after the keyboard!")
#print number_to_list(1234)
#print list_to_number([1, 2, 3, 4, 5, 6])
