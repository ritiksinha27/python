#Write a Python program to generate all permutations of a list in Python.

def perm():
    import itertools
    S=input("Enter the input list =")
    L=list(itertools.permutations(S.split(',')))
    print(L)

perm()
    
    
    