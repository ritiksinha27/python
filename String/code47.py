#Write a Python program to swap commas and dots in a string.


S=input("Enter the string with comma and dosts =")

S= S.replace(',','@')
S=S.replace('.',',')
S=S.replace('@','.')
print(S)