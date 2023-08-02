#Write a Python program to find the list of words that are longer than n from a given list of words.

S=input("Enter the list =")
L=S.split(',')
F=[]
n=int(input("enter the number n="))
for i in L:
    if len(i)>n:
        F.append(i)
print(F)