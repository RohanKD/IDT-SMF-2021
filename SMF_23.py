"""
Rohan Dalal
25 March 2021
IDT
1st Period
SMF_23
"""
#imported my smf 16 which had math functions
import SMF_16
# I made it a simpler word to use each time
fact = SMF_16.fact
divide = SMF_16.divide
log = SMF_16.log

def main():
# cant add a string and an int, this makes sure both are numbers
  try:
    x = int(input('Enter first number '))
    y = int(input('Enter second number '))
    print(x+y)
  except:
    print('Please enter two valid numbers')

# factorials can only be of positive integers
  try:
    a = int(input('What factorial do you want to compute?: '))
    print(fact(a))
  except:
      print('Please enter a positive integer')
# this protects against ZeroDivisionError
  b = int(input('First number to divide '))
  c = int(input('secind number to divide '))
  try:
    print(divide(b, c))
  except:
    print("Second number can't be 0")
#You cant take the log of a negative number, which this prevents
  d = int(input('What is the number '))
  e = int(input('What is the base '))
  try:
    print(log(d, e))
  except:
    print('Can not take the log of a negative number, please change the number.')

if(__name__ == '__main__'):
  main()
