#Write a Python program to extract numbers from a given string.
def num():
    S=input("Enter the string =")
    L=S.split(' ')
    x=''
    for i in L:
        if i.isnumeric()==True:
            x+=(i + ' ')
    print(x)
num()