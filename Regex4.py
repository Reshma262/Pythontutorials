#Program to extract maximum and minimum numerical value from a string. 

import re

def extract(str):
	numbers = re.findall('\d+',str)
	numbers = map(int,numbers)
	print(max(numbers))

str = input("Enter string ")
extract(str)