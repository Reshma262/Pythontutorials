#Program to find most recurring number in a string using Regex

import re
from collections import Counter

def maxfreq(str):
    a = re.findall(r'[0-9]+',str)
    maxf = 0
    maxe = 0
    c = Counter(a)
    for x in list(c.keys()):
        if c[x]>=maxf:
            maxf = c[x]
            maxe= x

    return maxe

str = input("Enter string ")
print(maxfreq(str))
