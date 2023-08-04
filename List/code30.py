#Write a Python program to get the frequency of elements in a list.

def freq():
    L=[int(x) for x in input("Enter the list =").split(',')]
    d={}
    for i in L:
        if i in d.keys():
            d[i]+=1
        else:
            d[i]=1
    print(d)
freq()