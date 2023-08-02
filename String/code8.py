#Write a Python program to remove the nth index character from a nonempty string.
S=input("Enter the string =")
n=int(input("Enter the nth term you want to remove"))

print(S[:n]+S[n+1:])