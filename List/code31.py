#Write a Python program to count the number of elements in a list within a specified range.

def rangenum():
    L=[int(x) for x in input("Enter the list =").split(',')]
    n=int(input("Enter the range ="))
    x=0
    for i in L:
        if i>=n:
            x+=1
    print(x)
rangenum()