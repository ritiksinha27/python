'''Write a Python function that takes a list of words and return the longest word and
the length of the longest one.'''

S=input("Enter the list of words")
L=S.split(',')
x=0
for i in L:
    if len(i)>x:
        x=len(i)
        a=i
