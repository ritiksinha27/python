#Write a Python program to extract and display the name from a given Email address.

def email():
    S=input("Enter the email id =")
    x=''
    y=''
    for i in range(len(S)):
        if S[i]=='@':
            x+=S[:i]
    for j in x:
        if j.isalpha()==True:
            y+=j

    print (y)
email()