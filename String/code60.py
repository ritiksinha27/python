#Write a Python program to capitalize the first and last letters of each word in a given string

def capital():
    S=input("Enter the string =")
    l=len(S)
    print(S[0].upper()+S[1:l-1]+S[l-1].upper())
capital()
        