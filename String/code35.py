#Write a Python program to format a number with a percentage.

def percent():
    n=float(input("enter the number ="))
    P="{:.2f}".format(n*100)
    print(P+'%')

percent()