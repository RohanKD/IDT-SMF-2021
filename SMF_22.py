"""
Rohan Dalal
25 March 2021
IDT
1st Period
SMF_23
"""

import os, sys

with open("Fortune500.txt") as file:

    def main():
        #setup variables defined
        lines = 0
        group = 0
        x = 0
        #For loop that assigns a value to each of the lines, and a design if needed at the end
        for line in file:
            lines += 1
            x = lines % 6
            if(x == 1):
                design= ''
                Description_type = 'Rank: '
            elif(x == 2):
                design = ''
                Description_type = 'Company Name: '
            elif(x == 3):
                design = ''
                Description_type = 'Revenues($M): '
            elif(x == 4):
                design = ''
                Description_type = 'Profits($M): '
            elif(x == 5):
                design = ''
                Description_type = 'Assets($M): '
            elif(x == 0):
                design = '\n' + '='*30
                Description_type = 'Market Value($M): '
            #each line is printed
            print((Description_type+ line + design))



    if(__name__ == '__main__'):
        main()
