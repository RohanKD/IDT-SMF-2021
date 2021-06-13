"""
Rohan Dalal
25 March 2021
IDT
1st Period
SMF_18 Module
"""

# series sum functions
# this one can calculate the sum of an inf geom series, if the raito is greater than one it diverges
def inf_geom_series(a, r):
    sum = a/(1-r)
    if(r>1):
        sum = 'The sum diverges to infinity'
    else:
        round(sum, 3)
    return sum

#this funstion calculates the sum of a finite arithmetic series
def sum_arithmetic_series(a, d, n):
    sum = (n/2)*(2*a + (n-1)*d)
    return sum

#this function calculates the sum of a finite geometric series
def finite_geom_series(a,r,n):
    sum = (a*(1-r**n))/(1-r)
    return sum
