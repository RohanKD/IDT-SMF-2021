"""
Rohan Dalal
23  February 2021
IDT
1st Period
SMF_10
"""
import cs50
import os,sys
import random

def main():

    #here i make a list
    print('Would you like to make a grocery list')
    print('You can add 5 items')
    groceryList=[]
    itemNumber= 1
    for i in range(5):
        x=input('What is item number '+ str(itemNumber))
        itemNumber=itemNumber+1
        groceryList.append(str(x))
    #Here the list is changed
    print('Your list is' +str(groceryList))
    print('Would you like to change item number one to orange')
    groceryList[0]= 'orange'
    print('Your new list is ' + str(groceryList))

    #Here I will make the tuple
    print('Do you like to make a shopping list')
    print('You can add 5 items')
    shoppingList=('pants', 'shirt', 'hoodie', 'hat', 'shoes' )
    print('Would you like to switch a hoodie for a jacket')
    #here i modify the tuple
    shoppingList= list(shoppingList)
    shoppingList[2]= 'jacket'
    shoppingList=tuple(shoppingList)
    print('You need to buy ' + str(shoppingList))
    #here i add the lists  to make a full list of things to buy
    shoppingList=list(shoppingList)
    fullList= shoppingList + groceryList
    print('Next time you go shopping make sure to buy these things ' + str(fullList))

if(__name__=='__main__'):
    main()
