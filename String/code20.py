#Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.

S=input("Enter the string =")
j=0
for i in range(4):
    if S[i].isupper()==True:
        j+=1
if j>=2:
    print(S.upper())
else:
    print(S)