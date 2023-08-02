#Write a Python program to find the second most repeated word in a given string.

def repeatword2():
    S=input("Enter the sentence =")
    L=S.split(' ')
    d={}
    F=[]
    V=[]
    for i in L:
        if i in d.keys():
            d[i]+=1
        else:
            d[i]=1
    for i in d.keys():
        if d[i] > 1:
            name=dict(sorted(d.items(), key= lambda x:x[1]))
            print(name)
            F+=name.keys()
            l=len(F) - 2
            print(F[l])
            break

repeatword2()