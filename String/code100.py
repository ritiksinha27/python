#Write a Python program to check whether any word in a given string contains duplicate characters or not. Return True or False.

def duplicate():
    S=input("Enter the string =")
    L=S.split(' ')
    x=''
    for i in L:
        d={}
        for j in i:
            if j in d.keys():
                d[j]+=1
                if i not in x:
                    x+=(i+' ')
            else:
                d[j]=1
    print(x)
    if x=='':
        print("True")
    else:
        print("False")
            
            
            
duplicate()