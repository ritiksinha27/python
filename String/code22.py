#Write a Python program to remove a newline in Python.
s=input('enter the sentence : ')
print(s)
b= r'\n'
a = s.strip(b)
print(a)