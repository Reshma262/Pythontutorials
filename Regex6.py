#Regex Program to check if string starts and ends with the same character
#Implementation of Regular Expression

import re

def check(str):
        if(re.search(r'^[a-z]$|^([a-z]).*\1$',str)): 
                print("Valid") 
        else: 
                print("Invalid") 
        
        

str = input("Enter string ")
check(str)
