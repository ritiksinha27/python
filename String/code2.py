#Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.

a=input("Enter the string = ")
if len(a)>1:
    print(a[0]+a[1]+a[len(a)-2]+a[len(a)-1])
else:
    print("Invalid string")