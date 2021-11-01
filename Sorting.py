#Sorting a list based on another list
#Implementing zip() function

def sortbysecond(l1,l2):
   l3 = zip(l2,l1)
   ans = [x for _, x in sorted(l3)]
   return ans

n = int(input("Enter size of array  "))
print("Enter elements of array1 ")
arr1 = []
for i in range (0,n):
    x = input()
    arr1.append(x)

print("Enter elements of array2 ")
arr2 = []
for i in range (0,n):
    x = input()
    arr2.append(x)

print(sortbysecond(arr1,arr2))
