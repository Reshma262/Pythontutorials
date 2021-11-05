#Exploring panda series


import pandas as pd

a = [3,7,2]
x = pd.Series(a)
print(x)
print(x[1])
x = pd.Series(a, index = ["x","y","z"])
print(x)
print(x["y"])
