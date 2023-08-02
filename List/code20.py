#Write a Python program to access the index of a list.

def index():
    L=[x for x in input("ENter the list =")]
    for i in range(len(L)):
        print("The index of ",L[i]," is ",i)
index()