#Write a Python program to clone or copy a list.
'''
L=[x for x in input("Enter the List =")]
S=list(L)
print(L,S)

OR if it has more than one character'''

A=input("Enter the list =")
L=A.split(',')
S=list(L)
print(L,S)