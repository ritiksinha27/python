#Write a Python program to move spaces to the front of a given string.
def spacefront():
    X=''
    Z=''
    S=input("Enter the string")
    for i in S:
        if i==' ':
            X+=i
        else:
            Z+=i
                
    print(X+Z)
spacefront()