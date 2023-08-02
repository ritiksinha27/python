#Write a Python program to print the following integers with zeros to the left of the specified width.

def zerotrail():
    import textwrap
    n=int(input("Enter the number ="))
    F="{:0>10d}".format(n)
    print(F)

zerotrail()