"""
Rohan Dalal
25  February 2021
IDT
1st Period
SMF_16
"""
import math


def fact(x):
    factorial = 1
    for i in range(2, x+1 ):
        factorial = factorial * i
    return factorial


def multiply(x, y):
    return x * y


def add(x, y):
    return x + y


def divide(x, y):
    return round((x / y), 3)


def subtract(x, y):
    return x - y


def exponent(x, n):
    a=x
    for i in range(n-1):
        x = x*a
    return x


def sqrt(x):
    return round(math.sqrt(x), 3)


def log(a, b):
    return round(math.log(a, b), 3)


def main():
    repeat = 0
    print('there are many functions you can do.')
    while (repeat == 0):
        function = input('What math function would you like to do, type the function. type leave to leave ')
        if (function == 'factorial'):
            x = int(input('What number do you want the factorial of'))
            print(fact(x))
        elif (function == 'multiply'):
            x = int(input('What is the first number'))
            y = int(input('What is the second number'))
            print(multiply(x, y))
        elif (function == 'add'):
            x = int(input('What is the first number'))
            y = int(input('What is the second number'))
            print(add(x, y))
        elif (function == 'subtract'):
            x = int(input('What is the first number'))
            y = int(input('What is the second number'))
            print(subtract(x, y))
        elif (function == 'divide'):
            x = int(input('What is the first number'))
            y = int(input('What is the second number'))
            print(divide(x, y))
        elif (function == 'exponent'):
            x = int(input('What is the number'))
            y = int(input('What is the power'))
            print(exponent(x, y))
        elif (function == 'sqrt'):
            x = int(input('What number would you like to square root'))
            print(sqrt(x))
        elif (function == 'log'):
            x = int(input('What is the number'))
            y = int(input('What is the base'))
            print(log(x, y))
        elif (function == 'leave'):
            repeat += 1
        else:
            print('Please enter a valid function, You may choose out of: add, subtract, multiply, divide, factorial, log, exponent, or sqrt')


if (__name__ == '__main__'):
    main()
