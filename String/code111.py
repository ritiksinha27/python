#Write a Python program that takes a string and replaces all the characters with their respective numbers.

def number():
    S=input("Enter the string =")
    A='abcdefghijklmnopqrstuvwxyz'
    x=''
    for i in range(len(S)):
        for j in range(len(A)):
            if A[j]==S[i]:
                print(S[i])
                x+=(str(j+1)+' ')
    print(x)
number()