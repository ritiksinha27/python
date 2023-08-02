#Write a Python program to find the smallest and largest words in a given string.

def leng():
    S=input("Enter the string =")
    L=S.split(' ')
    d={}
    Lf=[]
    for i in L:
        if i not in d.keys():
            d[i]=len(i)
    f= dict(sorted(d.items(), key=lambda x:x[1] ))
    for j in f:
        Lf.append(j)
    print("Smallest string is ",Lf[0])
    print("Largest string is ",Lf[-1])
    
    
    

leng()