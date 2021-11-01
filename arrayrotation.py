#python program to rotate an array of size n by d elements to the left

def rotate (arr, n, d):
    d = d % n
    arr2=[]
    for i in range(0,n):
        arr2.append(arr[i])
    for i in range (0,n):
        arr[i] = arr2[(i+d)%n]
    return arr

n = int(input("Enter size of array  "))
print("Enter elements ")
arr = []
for i in range (0,n):
    x = int(input())
    arr.append(x)

d = int(input("Enter d  "))
print(rotate(arr,len(arr),d))
