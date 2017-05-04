import operator
from itertools import cycle
from functools import reduce
from sympy import mpmath
from sympy.functions.combinatorial.numbers import nC


def dice_probability(n):
    """ Calculates the probability of an n-sided die to have all numbers
        in the list from 1 through n in a trial of n throws
        Input n : n-sided dies (Should be more than 1 and up to 120)
        Output probability : dice_probability
    """

    if not isinstance(n, int):
        raise ValueError('Input not of integer instance')
    if n < 1 :
        raise ValueError('Input not a positive integer')
    if n == 1 :
        raise ValueError('A dice can not have only 1 side. Minimum n =2')
    if n > 120 :
        raise ValueError('A dice can not have more than 120 sides')
    if n == '' :
        raise ValueError('Input can not be empty')

    exclusions_list = [(nC(n, r) * ((n-r)**n)) for r in range(n)]
    nr = reduce(operator.add,
                [x*y for x, y in zip(exclusions_list, cycle([1, -1]))])
    dr = n**n
    probability = mpmath.mpf(nr)/mpmath.mpf(dr)
    return probability

