"""
Rohan Dalal
23  February 2021
IDT
1st Period
SMF_13
"""
#Preprocessor directives
import math
import os, sys


def main():
    # here a finite arithmetic series is calculated.
    print('I will first show how to calculate the sum of and finite algebraic series using finite iteration and infinte iteration')
    print('All i need is the first term, last term and the common difference')
    first = int(input('Give the first term'))
    a = first
    last = int(input('Give the last term'))
    d = int(input('Give the common difference'))
    x = (last - first) / d + 1
    x = int(x)
    total = 0
    for i in range(0, x):
        total = total + first
        first = first + d
    # here an infinite iteration for the same sum is calcculated
    print(total)
    total = 0
    first = a
    while (first != last + d):
        total = total + first
        first = first + d
    print(total)
    print('As you can see both ways to sum an arithmetic sequence gave the same answer, we will know try the same thing with geometric sequences')
    # here finite iteration for a geometric sum.
    print('This time i will need the first, last term, and the common ratio')
    term1 = int(input('Give the first term in the sequence'))
    b = term1
    term_n = int(input('Give the last term in the sequence'))
    r = int(input('Give the common ratio'))
    n = math.log((term_n / term1), (r)) + 1
    n = int(n)
    geom_sum = 1
    for i in range(0, n-1):
        term1 *= r
        geom_sum += term1
    #here infinite iteration is used to calculate
    print(geom_sum)
    geom_sum = b
    term1 = b
    while (term1 != term_n):
        term1 *= r
        geom_sum += term1

    print(geom_sum)


if (__name__ == '__main__'):
    main()
