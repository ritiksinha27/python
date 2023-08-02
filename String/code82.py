#Write a Python program to wrap a given string into a paragraph with a given width.

def width():
    import textwrap
    S=input("Enter the string =")
    w=int(input("Enter the width ="))
    x=textwrap.fill(S,width=w)
    print(x)

width()    