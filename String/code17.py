#Write a Python function to get a string made of the first three characters of a specified string. If the length of the string is less than 3, return the original string.

S=input("Enter the string =")
if len(S)>=3:
    print(S[:3])
else:
    print(S)