#Write a Python program to remove duplicate characters from a given string.

def duplicate():
    S= input("Enter the string =")
    d={}
    L=[]
    st=''
    for i in S:
        if i in d.keys():
            d[i]+=1;
        else:
            d[i]=1
    L+=d.keys()    
    for i in L:
        st+=i
    print(st)
    

duplicate()