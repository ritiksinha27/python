#Write a Python program to split a string on the last occurrence of the delimiter.
S=input("enter the string =")
d=input("enter the delimiter")
l=[]
for i in S:
    if i == d : 
        l.append(S.index(i))
a= sorted(l)
c=S[0:a[-1]]
d=S[a[-1]+1:]
print(c)
print(d)