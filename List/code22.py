#Write a Python program to convert a list of characters into a string.
def index():
    L=[x for x in input("Enter the list =")]
    n=input("Enter the character =")
    for i in range(len(L)):
        if L[i]==n:
            print(i)
            
index()