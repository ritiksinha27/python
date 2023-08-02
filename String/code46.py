#Write a Python program to lowercase the first n characters in a string.

S=input("Enter the string =")
n=int(input("Enter the nth number you want to lower ="))
x= S[:n].lower() + S[n:]
print(x)