#Regex Program to put spaces between words beginning with capital letters and then convert uppercase to lower case letters

import re

def sentence(str):
        words = re.findall('[A-z][a-z]*', str)
        for i in range(0,len(words)):
                words[i] = words[i][0].lower()+words[i][1:]
        print(' '.join(words))

str = input("Enter string ")
sentence(str)
