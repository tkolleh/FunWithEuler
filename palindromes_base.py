""" Problem 1.
 Solve for the smallest base of a number where its a palindrome.
 So for 999 return 10 for base 10 and for 0 return 2 for base 2
"""

import math


def answer(n):
    if (n < 0 or n > 1000):
        raise Exception("Parameter out of bounds")

    base = 1
    palindrome = False
    while not palindrome:
        base += 1
        if is_palindrome(n, base):
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
