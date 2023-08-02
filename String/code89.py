#Write a Python program to remove unwanted characters from a given string.
def unwanted():
    S=input('Enter the String')
    p=''
    for i in S:
        if i.isalpha()== True:
            p+=i 
    print(p)