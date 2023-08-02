#Write a Python program to shuffle and print a specified list.
def shuf():
    from random import shuffle
    L=[x for x in input("enter a list =")]
    shuffle(L)
    print(L)
shuf()