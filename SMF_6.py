"""
Rohan Dalal
27 January 2021
IDT
1st Period
SMF_6
"""
import os,sys
import math
import cs50

def Area():
    print('This is a triangle area calculator, It can find the area through herons formula, no matter the angles or size.')
    a= int(input('Enter length of the first side:'))
    b= int(input('Enter length of the second side:'))
    c= int(input('Enter length of the third side:'))

    if (((a+b)<= c) or ((b+c)<= a) or ((a+c)<=b)):
        print("please try again, these side lengths don't make a real triangle")
    else:
        s = (a+b+c)/2
        areaSquared = (s)*(s-a)*(s-b)*(s-c)
        Area = math.sqrt(areaSquared)
        print('The area is '+str(Area) )
if(__name__=='__main__'):
    main()
