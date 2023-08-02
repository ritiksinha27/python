#Write a Python program to generate two strings from a given string. For the first string, use the characters that occur only once, and for the second, use the characters that occur multiple times in the said string.

def multiple():
    S=input("Enter the string =")
    d={}
    x=''
    y=''
    for i in S:
        if i in d.keys():
            d[i]+=1
        else:
            d[i]=1
    for j in d.items():
        if j[1]>1:
            x+=j[0]
        else:
            y+=j[0]
    print("repeated string =",x)
    print("Non repeated string =",y)
 
multiple()