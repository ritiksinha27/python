#Write a Python program to sum all the items in a list.

S=input("Enter the list =")
L=S.split(' ')
x=0
for i in range(len(L)):
    x += int(L[i]) 
print(x)