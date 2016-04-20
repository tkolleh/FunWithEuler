import math


def answer(n):
    if (n < 0 or n > 1000):
        raise Exception("Parameter out of bounds")

    b_number = int(str(bin(n))[2:])
    base = 1
    palindrome = False
    while not palindrome:
        base += 1
        if base == 10:
            if is_palindrome(n, base):
                palindrome = True
        elif is_palindrome(b_number, int(str(bin(base))[2:])):
                palindrome = True

    return base


def is_palindrome(number, base):
    forward = number
    rev = 0
    while number > 0:
        digit = math.floor(number % base)
        rev = rev * base + digit
        number = math.floor(number / base)

    return (forward == rev)

num = 0
while num < 1002:
    print('Palindrome base for '+str(num)+' is '+str(answer(num)))
    num += 1

# print('Palindrome for 0 is '+str(answer(0)))
# print('Palindrome for 3 is '+str(answer(3)))
# print('Palindrome for 42 is '+str(answer(42)))
# print('Palindrome for 97 is '+str(answer(97)))
# print('Palindrome for 999 is '+str(answer(999)))
#print('Palindrome for 1097 is '+str(answer(1097)))
