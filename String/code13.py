#Write a Python program that accepts a comma-separated sequence of words as input and prints the distinct words in sorted form

S=input('Enter the values using comma =')
L=S.split(',')
L.sort()
print(L)