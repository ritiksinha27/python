#Write a Python program to swap cases in a given string.

def convert():
    S=input("Enter the string =")
    x=''
    for i in S:
        if i.isupper():
            x+=(i.lower())
        elif i.islower():
            x+=(i.upper())
    print(x)

convert()