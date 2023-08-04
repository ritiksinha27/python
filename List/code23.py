#Write a Python program to flatten a shallow list.

def flat():
    L=[int(x) for x in input("Enter the list =") if x.isnumeric()==True]
    print(L)
flat()