'''Write a Python program to count repeated characters in a string.
Sample string: 'thequickbrownfoxjumpsoverthelazydog'
Expected output :
o 4
e 3
u 2
h 2
r 2
t 2'''

S=input("Enter the string =")
d={}
for i in S:
    if i in d.keys():
        d[i]+=1
    else:
        d[i]=1
for j in d.keys():
    if d[j]>1:
        print(j,d[j])