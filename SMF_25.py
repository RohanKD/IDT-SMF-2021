"""
Rohan Dalal
6 April 2021
IDT
1st Period
SMF_25
"""
import math
# finds the magnitude and direction of a vector that is given in component form
Magnitude = lambda x, y: math.sqrt(x ** 2 + y ** 2)
Direction = lambda x, y: math.atan(y / x)


def degree(x):
    pi = 3.1415926535897932384626466
    d = x * 180 / pi
    return d


def main():
    i = 0

    while (i < 4):
        i += 1
        x = int(input('What is the x-coord of the point'))
        y = int(input('What is the y-coord of the point'))
        if (x == 0):
            print('The magnitude of the vector from the origin to this point is: ' + str(
                round(Magnitude(x, y), 3)) + ' and the angle is: 90 degrees')
        else:
            print('The magnitude of the vector from the origin to this point is: ' + str(
                round(Magnitude(x, y), 3)) + ' and the angle is: ' + str(
                round(degree(Direction(x, y)), 3)) + ' degrees')


if (__name__ == '__main__'):
    main()
