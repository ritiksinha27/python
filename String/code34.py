#Write a Python program to display a number with a comma separator.

def comma():
    n=int(input("enter the number ="))
    F="{:,}".format(n)
    print(F)

comma()