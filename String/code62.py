#Write a Python program to compute the sum of the digits in a given string.

def sum():
    S=input("Enter the string =")
    n=0
    for i in S:
        if i.isdigit():
            n=n+int(i)
    print(n) 

sum()           