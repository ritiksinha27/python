#Write a Python program to add prefix text to all of the lines in a string.

S=int(input("enter the number of lines ="))
F=[]
for i in range(S):
    x=input("enter the string =")
    F.append(x + '\n')
print(F)

