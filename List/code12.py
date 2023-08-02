#Write a Python program to print a specified 
# list after removing the 0th, 4th and 5th elements.

A=input("Enter the list =")
L=A.split(',')
S=[]
for i in L:
    S.append(i)
S.remove(S[5])

S.remove(S[4])

S.remove(S[0])

print(L,S)
