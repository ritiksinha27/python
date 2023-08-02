#Write a Python program to find the maximum number of characters in a given string.

S=input("enter the string =")
d={}
for i in S:
    if i in d.keys():
        d[i]+=1
    else:
        d[i]=1
v = list(d.values())

k = list(d.keys())
 
print(k[v.index(max(v))],v[v.index(max(v))])