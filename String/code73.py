#Write a Python program to count Uppercase, Lowercase, special characters and numeric values in a given string.

def count():
    S=input("Enter the string =")
    upper=0
    lower=0
    special=0
    numeric=0
    for i in S:
        if i.isupper():
            upper+=1
        elif i.islower():
            lower+=1
        elif i.isdigit():
            numeric+=1
        else:
            special+=1
    
    print( lower,"lower",'\n',upper , "upper",'\n',special,"special" ,'\n',numeric,"numeric")

count()