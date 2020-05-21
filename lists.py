# import timeit
# def make_word_list():
#     words = []
#     file = open('example.csv')
#     for row in file:
#         word = row.split(';')
#         words.append(word)
#
#     return words
#
#
# def make_word_list_additional():
#     words = []
#     file = open('example.csv')
#     for row in file:
#         word = row.split(';')
#         words += [word]
#     return words
#
#
# def make_word_list():
#     """Reads lines from a file and builds a list using append.
#
#     returns: list of strings
#     """
#     word_list = []
#     fin = open('words.txt')
#     for line in fin:
#         word = line.strip()
#         word_list.append(word)
#     return word_list
#
#
# def in_bisect(ordered_list, value):
#     count = len(ordered_list)
#     if count == 0:
#         return False
#
#     i = count // 2
#
#     if ordered_list[i] == value:
#         return True
#
#     if ordered_list[i] > value:
#         return in_bisect(ordered_list[:i], value)
#     else:
#         return in_bisect(ordered_list[i+1:], value)
#
#
# def find_reverse_pairs(words):
#     pairs = []
#     word_list = words[:]
#     for i, word in enumerate(word_list):
#         reverse = word[::-1]
#         print(reverse)
#         word_list.remove(word)
#         if reverse in word_list:
#             pairs.append([word, reverse])
#     print(pairs)
#     return pairs
#
# def original_fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return original_fib(n-1) + original_fib(n-2)
#
# memorized = {0: 0,
#              1: 1}
#
# def memorized_fib(n):
#     if n in memorized:
#         return memorized[n]
#     res = memorized_fib(n-1) + memorized_fib(n-2)
#     memorized[n] = res
#     return res
#
# if __name__ == '__main__':
#     import time
#     started = time.time()
#     print(original_fib(40))
#     print(time.time()-started)
    #
    # started1 = time.time()
    # print(memorized_fib(40))
    # print(time.time()-started1)
    # word_list = ["lol", "ohlol", "lolho", "ababab", "bababa", "ululd", "dlulu", "artem", "ror", "ror"]
    # find_reverse_pairs(word_list)
    #
    # started = timeit.timeit()
    # make_word_list()
    # ended = timeit.timeit()
    # print(ended-started)
    # #
    # started = timeit.timeit()
    # make_word_list_additional()
    # ended = timeit.timeit()
    # print(ended-started)


    # t = [0, 13, 22, 1, 5, 10, 9, 8, 6, 5, 4]
    # t.sort()
    # print(t)



# if __name__ == '__main__':
    # word_list = make_word_list()
    #
    # for word in ['aa', 'alien', 'allen', 'zymurgy']:
    #     print(word, 'in list', in_bisect(word_list, word))
    #
    # for word in ['aa', 'alien', 'allen', 'zymurgy']:
    #     print(word, 'in list', in_bisect_cheat(word_list, word))


"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import bisect


def make_word_list():
    """Reads lines from a file and builds a list using append.

    returns: list of strings
    """
    word_list = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        word_list.append(word)
    return word_list


def in_bisect(word_list, word):
    """Checks whether a word is in a list using bisection search.

    Precondition: the words in the list are sorted

    word_list: list of strings
    word: string

    returns: True if the word is in the list; False otherwise
    """
    if len(word_list) == 0:
        return False

    i = len(word_list) // 2
    if word_list[i] == word:
        return True

    if word_list[i] > word:
        # search the first half
        return in_bisect(word_list[:i], word)
    else:
        # search the second half
        return in_bisect(word_list[i + 1:], word)


def in_bisect_cheat(word_list, word):
    """Checks whether a word is in a list using bisection search.

    Precondition: the words in the list are sorted

    word_list: list of strings
    word: string
    """
    i = bisect.bisect_left(word_list, word)
    if i == len(word_list):
        return False

    return word_list[i] == word



def nested_sum(l):
    ttl_sum = 0
    for item in l:
        if not isinstance(item, list):
            item = [item, ]
        ttl_sum += sum(item)
    return ttl_sum


def cum_sum(t):
    count = len(t)
    if count == 0:
        return t
    result_t = list()
    for i in range(count):
        result_t.append(sum(t[:i+1]))
    return result_t


def middle(t):
    return t[1:-1]


def is_sorted(l):
    if len(l) == 0:
        return None

    if l[0] > l[1]:
        return False
    else:
        return True


def is_anagrams(word1, word2):
    for char in word1:

        if char not in word2 or word1.count(char) != word2.count(char):
            return False
        else:
            return True


def read():
    results = []
    with open('words.txt', 'r') as fin:
        for line in fin.readlines():
            word = line.strip()
            results += [word]
    return results

def is_bisect(word, word_list):
    print("Iteration")
    middle = len(word_list) // 2
    if middle == 0:
        if word_list[0] == word:
            return True
        else:
            return False
    if word_list[middle] == word:
        return word
    if word > word_list[middle]:
        return is_bisect(word, word_list[middle:])
    else:
        return is_bisect(word, word_list[:middle+1])

def interlock(*args):
    interlock = ''

    for i in range(len(args[0])):
        for word in args:
            interlock += word[i]

    return interlock

def reverse_pair(words):
    for word in words:
        word_reversed = word[::-1]
        if is_bisect(word_reversed, words):
            print(word, word_reversed)

if __name__ == '__main__':
    words_l = read()
    print(words_l)
    print(len(words_l))
    # reverse_pair(words_l)
    print(is_bisect('disendows', words_l))
    # word1 = "shoe"
    # word2 = "cold"
    # word3 = "tits"
    # print(interlock(word1, word2, word3))