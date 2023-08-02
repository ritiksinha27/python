#Write a Python program to decapitalize the first letter of a given string.
def decapital():
    S=input("Enter the string =")
    x=''
    for i in range(len(S)):
        if i==0:
            x+=S[i].lower()
        else:
            x+=S[i]
    print(x)

decapital()