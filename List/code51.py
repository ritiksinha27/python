# Write a Python program to split a list every Nth element.
def slicing():
    L=[x for x in input("Enter the list =")]
    x=''
    n=int(input("enter the nth value -"))
    for i in range(n):
        print(L[i::n])
slicing()
    