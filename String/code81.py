#Write a Python program to determine the index of a given 
# string at which a certain substring starts. 
# If the substring is not found in the given string return 'Not found'.

def index():
    S=input("Enter the string =")
    n=input("enter the substring =")
    index=0
    for i in range(len(S)):
        if S[i]==n:
            index=i
        
    print(index)

index()