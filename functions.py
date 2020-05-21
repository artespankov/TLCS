import math
from functools import reduce
import random
# import turtle
# import time
#
# def find_epoch():
#     epoch = time.time()
#
#     day_in_secs = (60*60*24)
#
#     days = epoch // day_in_secs
#     seconds_passed_today = epoch % day_in_secs
#     print(seconds_passed_today)
#     print("Days since: ", days)
#
#     hours = seconds_passed_today // (60*60)
#     minutes = (seconds_passed_today % (60*60)) // 60
#     seconds = seconds_passed_today - hours*60*60 - minutes*60
#
#
#     print("Hours: ", hours+2)
#     print("Minutes: ", minutes)
#     print("Seconds: ", seconds)
#
#
# def check_fermat(a, b, c, n):
#
#     if n > 2:
#         print(pow(a, n) + b**n)
#         print(c**n)
#         if pow(a, n) + b**n == c**n:
#             print("Holy smokes, Fermat was wrong!")
#             return
#     print("No, that doesn’t work.")
#
#
# def draw(t, length, n):
#     if n == 0:
#         return
#     angle = 50
#     t.fd(length*n)
#     t.lt(angle)
#     draw(t, length, n-1)
#     t.rt(2*angle)
#     draw(t, length, n-1)
#     t.lt(angle)
#     t.bk(length*n)
#
#
# def is_triangle(a, b, c):
#     if a < b+c and b < a+c and c < a+b:
#         print("Yes")
#         return
#     print("No")
#
#
# def recurse(n, s):
#
#     """
#     :param n: positive integer
#     :param s:
#     :return: sum of numbers 1 .. n
#     """
#     if n == 0:
#         print(s)
#     else:
#         recurse(n-1, n+s)
#
#
# def koch(t, n):
#     if n < 10:
#         t.fd(n)
#         return
#     m = n/3
#     koch(t, m)
#     t.lt(60)
#     koch(t, m)
#     t.rt(120)
#     koch(t, m)
#     t.lt(60)
#     koch(t, m)
#
#
# def fact(n):
#     if n == 0:
#         return 1
#     return n*fact(n-1)
#
#
# def ack(m, n):
#     result = 1
#     if m == 0:
#         return result * n+1
#     if m > 0 and n == 0:
#         return result*ack(m-1, 1)
#     if m>0 and n>0:
#         return result*ack(m-1, ack(m, n-1))


# def first_letter(string):
#     return string[0]
#
#
# def last_letter(string):
#     return string[-1]
#
#
# def inner(string):
#     return string[1:-1]
#
# def is_palindrome(string):
#     if len(string) <= 1:
#         return True
#     if first_letter(string) != last_letter(string):
#         return False
#     else:
#         return is_palindrome(inner(string))
#
#
# def b(z):
#     prod = a(z, z)
#     print(z, prod)
#     return prod
#
#
# def a(x, y):
#     x = x + 1
#     return x * y
#
#
# def c(x, y, z):
#     total = x + y + z
#     square = b(total) ** 2
#     return square

#
# def is_power(a, b):
#     if a <= 0:
#         return False
#     if a % b == 0:
#         return True
#     return is_power(a/b, b)
#
#
# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)


# def print_n(n):
#     print(n)
#     while n >= 0:
#         print(n)
#         n -= 1
#
#
# def mysqrt(a):
#     epsilon = 0.0000001
#     x = a - a*0.5
#     while True:
#         y = (x + a/x)/2
#         if abs(y-x) < epsilon:
#             break
#         x = y
#     return y
#
#
# def test_sqrt():
#     for a in range(1, 10):
#         print("a: {} ; ".format(a),
#               "sqrt(): {} ; ".format(math.sqrt(a)),
#               "mysqrt(): {} ; ".format(mysqrt(a)),
#               "diff(): {} ; ".format(math.sqrt(a) - mysqrt(a))
#               )
#
# def factorial(n):
#     """Computes factorial of n recursively."""
#     if n == 0:
#         return 1
#     else:
#         recurse = factorial(n-1)
#         result = n * recurse
#         return result
#
#
# def estimate_pi():
#     """Computes an estimate of pi.
#
#     Algorithm due to Srinivasa Ramanujan, from
#     http://en.wikipedia.org/wiki/Pi
#     """
#     total = 0
#     k = 0
#     factor = 2 * math.sqrt(2) / 9801
#     while True:
#         num = factorial(4 * k) * (1103 + 26390 * k)
#         den = factorial(k) ** 4 * 396 ** (4 * k)
#         term = factor * num / den
#         total += term
#
#         if abs(term) < 1e-15:
#             break
#         k += 1
#
#     return 1 / total
#
#
# def eval_loop():
#     result = None
#     while True:
#         expression = input("Enter an expression to evaluate: ")
#         if expression == 'done':
#             print(result)
#             break
#         else:
#             result = eval(expression)
#             print(result)
#
# def make_names():
#     prefixes = 'JKLMNOPQ'
#     secondary_prefixes = 'OQ'
#     suffix = 'ack'
#
#     for letter in prefixes:
#         if letter in secondary_prefixes:
#             print(letter + 'u' + suffix)
#         else:
#             print(letter+suffix)
#
#
# def find(string, letter, index=0):
#     for i in range(index, len(string)):
#         if string[i] == letter:
#             print(i)
#             return i
#         i += 1
#     print(-1)
#     return -1
#
# def count(string, letter, index=0):
#     i=0
#     for char in string[index:]:
#         if char == letter:
#             i += 1
#     print(i)
#
# def is_palindrome(string):
#     return string[::-1] == string
#
#
# def rotate(word, pos):
#     cypher = ''
#     for char in word:
#         print(ord(char))
#         print(chr(ord(char) + pos))
#         cypher += chr(ord(char) + pos)
#     print(cypher)
#
#
# def nested_sum(nested_l):
#     summary = 0
#     for sub_l in nested_l:
#         for item in sub_l:
#             summary += item
#
#     return summary


# def cum_sum(t):
#     new_one = []
#     for i in range(1, len(t)):
#         summary = reduce(lambda x, y: x+y, t[:i])
#         new_one.append(summary)
#     return new_one
#
#
# def middle(l):
#     return l[1:-1]
#
#
# def chop(l):
#     del l[0]; del l[-1]
#     return l
#
# def is_sorted(l):
#     if l[0] > l[-1]:
#         return False
#     for i in range(0, len(l)-1):
#         print(l[i])
#         if l[i] > l[i+1]:
#             return False
#     return True


def is_anagram(word1, word2):
    word1 = word1.lower().replace(' ', '')
    word2 = word2.lower().replace(' ', '')
    for letter in word1:
        if letter not in word2 or word1.count(letter) != word2.count(letter):
            print(letter)
            return False
    return True


def has_duplicates(t):
    l = t[:]
    for i in range(len(l)-1):
        print(i)
        letter = l.pop(i)
        if letter in l:
            print("It has")
            return True
    print("No, it doesn't")
    return False


def factorial(n):
    if n <= 0:
        return 1
    return factorial(n-1)


def check_birthday_probability(n):
    k = 365
    binominal_koeff = factorial(n) / (factorial(k) * factorial(n-k))
    probability = factorial(n) * binominal_koeff / k**n
    print(probability)
    return probability


def random_bdays(n):
    """Returns a list of integers between 1 and 365, with length n.

    n: int

    returns: list of int
    """
    t = []
    for i in range(n):
        bday = random.randint(1, 365)
        t.append(bday)
    return t

def count_matches(num_students, num_simulations):
    """Generates a sample of birthdays and counts duplicates.

    num_students: how many students in the group
    num_samples: how many groups to simulate

    returns: int
    """
    count = 0
    for i in range(num_simulations):
        t = random_bdays(num_students)
        if has_duplicates(t):
            count += 1
    return count

def find_interlocks(word1, word2):
    resulting = ''
    if len(word1) != len(word2):
        return

    for i in range(0, len(word1)):
        resulting += word1[i]
        resulting += word2[i]

    return resulting


def fib(n=2):
    a, b = 1, 1
    while a <= n:
        print(a)
        a, b = b, a+b
    print(' ')




if __name__ == "__main__":
    # # t = [[1, 2], [3], [4, 5, 6]]
    # # print(nested_sum(t))
    # t = [1, 2, 3, 4, 5, 6]
    # # print(cum_sum(t))
    # print(middle(t))
    # print(chop(t))
    # print(t)
    #
    # print(is_sorted())
    # has_duplicates([1, 2, 5, 2, 5, 2])
    # has_duplicates([1, 2, 5])
    #
    # print(is_anagram('Damon Albarn', 'Dan Abnormal'))
    #
    # print(is_anagram('Madonna Louise Ciccone',  'One cool dance musician'))
    #
    # birthdays = [random.randrange(10, 20) for _ in range(23)]
    #
    # check_birthday_probability(len(birthdays))

    # count('aaaa', 'a')
    # count('gfghjkl', 'a')
    # count('gfghjkl', 'k', index=3)
    # count('gfghjkl', 'k', index=len('gfghjkl'))



    # print(is_power(121, 11))

    # a = int(input("Type A: "))
    # b = int(input("Type B: "))
    # c = int(input("Type C: "))
    #
    # is_triangle(a, b, c)

    # (a, b, c, n) = [int(argument) for argument in input("Input 4 numbers separated with comma: ").split(',')]
    # check_fermat(a, b, c, n)
    # bob = turtle.Turtle()
    # draw(bob, 7, 14)
    # turtle.mainloop()

    # find_epoch()

    # recurse(-1, 10)
    # length = int(input("Set the length of Koch curve:"))
    #
    # bob = turtle.Turtle()
    #
    #
    #
    # for i in range (12):
    #     koch(bob, length)
    #     bob.rt(30)
    # n = int(input("Put the number to find it's factorial"))
    # print(fact(n))

    # print(ack(4, 5))
    # turtle.mainloop()
    # print(is_palindrome('urururu'))
    #
    #
    #
    #
    # x = 1
    # y = x + 1
    # print(c(x, y + 3, x + y))

    fib()