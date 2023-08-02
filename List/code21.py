#Write a Python program to convert a list of characters into a string.

def convert():
    x=''
    L=[x for x in input("Entert te list =")]
    for i in L:
        x+=i
    print("List is-",L)
    print("String is -",x)
convert()