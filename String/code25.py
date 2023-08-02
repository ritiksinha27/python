#Write a Python program to display formatted text (width=50) as output
import textwrap

S=input("Enter the string =")
F=textwrap.fill(S,width=10)
print(F)