#Write a Python program to find the first repeated character in a given string.

def repeat():
    S=input("Enter the string =")
    d={}
    for i in S:
        if i in d.keys():
            d[i]+=1
        else:
            d[i]=1
    for i in d.keys():
        if d[i] > 1:
            print(i)
            break

repeat()