#Write a Python program to remove spaces from a given string.

def space():
    Y=''
    S=input("Enter the string =")
    for i in S:
        Y+=i 
        Y=S.replace(' ','')
    print(Y)
        
space()