#Write a Python program to remove duplicate words from a given string.
def remove():
    S=input("Enter the string =")
    L=S.split(' ')
    L1=''
    d={}
    for i in L:
        if i in d.keys():
            d[i]+=1
            
        else:
            d[i]=1
            L1+=(i+' ')
    print(L1)

remove()