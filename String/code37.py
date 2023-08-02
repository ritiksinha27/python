#Write a Python program to count occurrences of a substring in a string.

def substring():
    S=input("Enter the string =")
    T=input("Enter the substring =")
    x=0
    for i in range(len(S)):
        if S[i:i+(len(T))]==T:
            x=x+1
        
    print(x)

substring()
        