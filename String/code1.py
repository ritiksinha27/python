#Write a Python program to count the number of characters (character frequency) in a string.

a=input("Enter the input")
d={}
for i in a:
    if i in d.keys():
        d[i]+=1
    else:
        d[i]=1
print(d)