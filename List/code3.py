#Write a Python program to get the largest number from a list.
''' n=int(input("Enter the no of input ="))
L=[]
for i in range(n):
    a=int(input("enter the input"))
    L.append(a)
m=max(L)
print(m)'''

'''or'''

S=input("Enter the list =")
x=S.split(',')
L=[int(a) for a in x]
m=max(L)
print(m)

'''OR

n=int(input("Enter the no of input ="))
L=[]
for i in range(n):
    L+=[int(input("Enter the input number"))]
m=max(L)
print(m)'''