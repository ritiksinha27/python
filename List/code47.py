#Write a Python program to insert an element before each element of a list.

def insert():
    L=[x for x in input("Enter the list =")]
    S=[]
    for i in L:
        S+=('@'+i)
    print(S)
insert()