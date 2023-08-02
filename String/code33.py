#Write a Python program to print the following integers with '*' to the right of the specified width.

def signtrail():
    import textwrap
    n=input("Enter the number =")
    w=int(input("Enter the width ="))
    #F="{:.2f}".format(n, w)
    b='*' *(w-len(n))
    print(n+b)
    

signtrail()