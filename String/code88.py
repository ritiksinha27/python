#Write a Python program to check whether a given string contains a capital letter, a lower case letter, a number and a minimum length.

def valid():
    S=input("Enter the string =")
    u=0
    l=0
    n=0
    for i in S:
        if i.isupper()==True:
            u+=1
        elif i.islower()==True:
            l+=1
        elif i.isdigit()==True:
            n+=1
    if u>0 and l>0 and n>0:
        print("Valid String")
    else:
        print("String not valid")

valid()