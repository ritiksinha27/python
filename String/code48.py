#Write a Python program to count and display vowels in text.
S=input("Enter the string =")
d={'a':0,'e':0,'i':0,"o":0,'u':0}
for i in S:
    if i in d.keys():
        d[i]+=1
print(d)