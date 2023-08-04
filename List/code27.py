#Write a Python program to find the second smallest number in a list.

def secondsmall():
    S=input("ENter the list =")
    
    L=[int(x) for x in S.split(',')]
    N=sorted(L)
    print(N[1])
    
secondsmall()