#Write a Python program to find the first non-repeating character in a given string.

def nonrepeat():
    S=input("Enter the string =")
    d={}
    for i in S:
        if i in d.keys():
            d[i]+=1
        else:
            d[i]=1
    print(d)
    for i in d.keys():
        if d[i]==1:
            x=i
            print(x)
            break


nonrepeat()
            