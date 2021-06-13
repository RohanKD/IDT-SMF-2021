"""
Rohan Dalal
25 March 2021
IDT
1st Period
SMF_20 Module
"""
#probabilty functions using factorials, some series use factorials, so it serves a dual purpose
def fact(x):
    total = 1
    for i in range(1, int(x)+1):
        total*=i
    return int(total)


#factorial function is called inside of permutation and combination functions
def Comb(n, r):
    outcomes = fact(n)/(fact(n-r)*fact(r))
    return int(outcomes)

def Perm(n, r):
    outcomes = (fact(n))/(fact(r))
    return int(outcomes)


#card probability

hearts = 13
clubs = 13
spades = 13
diamonds = 13
red = 26
black = 26
total = 52
face_suit = 3
face_total = 12

def prob_replacement(num_of_draws, card_type):
    probability = (int(card_type)/52)**(int(num_of_draws))
    return probability


def prob_no_replacement(num_of_draws, card_type):
    numerator = Perm(int(card_type), int(card_type)-int(num_of_draws))
    denominator = Perm(52, 52-int(num_of_draws))
    probability = numerator/denominator
    return float(probability)




