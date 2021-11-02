#Regex Program to check for a sequence in a string
#Here the sequence is one that has an uppercase letter followed by lower case letters

import re

def check(str):
        if(re.search('[A-Z]+[a-z]+$',str)): 
                print("Valid") 
        else: 
                print("Invalid") 
        
        

str = input("Enter string ")
check(str)
