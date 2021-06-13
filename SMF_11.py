"""
Rohan Dalal
23  February 2021
IDT
1st Period
SMF_11
"""
import cs50
import os,sys
import random

def main():
    print('This is an auto grading system, the rules are: No two people can have the same grade, and all the grades are between 90 and 100')
#the grades are rolled, and the set is created to test if multiple people got the same grade
    x= 90 + random.randint(0,10)
    y=90 + random.randint(0,10)
    z=90+ random.randint(0,10)
    grade={ 'John' : x, 'Rohan': y, 'Charles': z}
    test={}
    test=set(test)
    for key in grade:
       test.add(grade[key])
    t=0
    print('The grades are '+ str(x)+', ' +str(y)+', '+str(z) +'.')
    #this while loop tests if the length of the set is 3, which means that all three people had different grades.
    #if the length of the set is less than 3 it rerolls the grades until they are all distinct
    while(len(test)!=3):

        x= 90 + random.randint(0,10)
        y=90 + random.randint(0,10)
        z=90+ random.randint(0,10)
        grade={ 'John' : x, 'Rohan': y, 'Charles': z}
        test={}
        test=set(test)
        for key in grade:
           test.add(grade[key])
        t=t+1
        if(t>0):
            print('Two people had the same grade, so the grades were rerolled')
            print(test)
#here the dictionary is altered
    print("The teacher feels that the test was too hard, therefore he adds 3 points to each person's grade")
    for key in grade:
        grade[key]+=3
    print("After the change, here are each person's grades: " + str(grade))
    print("The teacher then realizes that Rohan's code is very good, so he changes his grade to a 105 ")
    grade['Rohan']=105
    print("After rohan's grade increase, here are each person's grades: " + str(grade))
if(__name__=='__main__'):
    main()
