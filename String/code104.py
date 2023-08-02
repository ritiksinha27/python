#Write a Python program that capitalizes the first letter and lowercases the remaining letters in a given string.
'''
def lower():
    S=input("Enter the string =")
    x=''
    for i in range(len(S)):
        if i==0:
            x+=S[0].upper()
        else:
            x+=S[i].lower()
    print(x)
lower()'''

S="Ritik sInha KUMAR"
L=' '.join(word.capitalize() for word in S.split())
print(L)
