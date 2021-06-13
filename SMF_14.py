"""
Rohan Dalal
25  February 2021
IDT
1st Period
SMF_15/16
"""
import math
import matplotlib.pyplot as plt

def Heron(a,b,c):
    if (((a+b)<= c) or ((b+c)<= a) or ((a+c)<=b)):
        Area = 0
     else:
        s = (a+b+c)/2
        areaSquared = (s)*(s-a)*(s-b)*(s-c)
        Area = math.sqrt(areaSquared)
        print('The area is '+str(Area))
        return Area

def Lengths(a,b,c,x,y,z):
    a= math.sqrt((c-a)*(c-a)+(x-b)*(x-b))
    b= math.sqrt((y-c)*(y-c)+(z-c)*(z-c))
    a= math.sqrt((a-y)*(a-y)+(b-z)*(b-z))
    return Heron(a,b,c)


def main:
    loop=0
    while(loop==0):
        
       x1= input('what is the x-coordinate of the first point')
       y1= input('what is the y-coordinate of the first point')
       x2= input('what is the x-coordinate of the second point')
       y2= input('what is the y-coordinate of the second point')
       x3= input('what is the x-coordinate of the third point')
       y3= input('what is the y-coordinate of the third point')
    print('The area of that triangle is ' + str(Heron(x1,y1,x2,y2,x3,y3))))


       

    
    
    
    
if(__name__=='__main__'):
    main()
