# Utility functions.

from copy import deepcopy as copy


def joinLists(lists):
    sum = []
    for list in lists:
        sum += list
    return sum


def sumByTerm(lists):
    l = len(lists)
    ls = len(lists[0])
    sum = [0] * ls

    for i in range(l):
        for j in range(ls):
            sum[j] += lists[i][j]

    return sum


def sum(list):
    sum = 0
    for x in list:
        sum += x
    return sum


def multTerms(mult, list):
    return [mult * k for k in list]


def invTerms(list):
    return [1 / k for k in list]


def multByTerm(lists):
    l = len(lists)
    ls = len(lists[0])
    mult = [1] * ls

    for i in range(l):
        for j in range(ls):
            mult[j] *= lists[i][j]

    return mult


def map(f, l): return [f(k) for k in l]


def avg(list): return sum(list)/len(list)


def sumAndAvg(list):
    s = sum(list)
    return s, s/len(list)


def clamp(x, smallest=0, largest=1): return max(smallest, min(x, largest))
