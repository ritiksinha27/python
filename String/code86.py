#Write a Python program to delete all occurrences of a specified character in a given string.
def replace():
    S=input("Enter the string =")
    n=input("Enter the character to be removed =")
    x=''
    for i in S:
        print(i)
        if i in n and i not in x:
            x+=S.replace(n,'')
            print(x)
            break

replace()