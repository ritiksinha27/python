#Write a Python program to multiply all the items in a list.

S=input("enter the list =")
L=S.split(',')
x=1
for i in range(len(L)):
    x *= int(L[i]) 
print(x)