#Write a Python program to remove duplicates from a list.

S=input("Enter the list")
L=S.split(',')
Y=list(dict.fromkeys(L))
print(Y)