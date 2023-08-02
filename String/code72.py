#Write a Python program to remove all characters except a specified character from a given string.

def remove():
    S=input("Enter the string =")
    n=input("enter the specified string =")
    x=''
    y=''
    for i in S:
        if i==n:
            x+=i
        else:
            y+=i
    print(x)

remove()