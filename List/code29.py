#Write a Python program to get unique values from a list.

def unique():
    S=input("Enter the list =")
    L=[int(x) for x in S.split(',')]
    F=set(L)
    print(F)
unique()