# Write a Python program to add two strings as if they were numbers (positive integer values). Return a message if the numbers are strings.

def add():
    n1=input("Enter the number 1 =")
    n2=input("Enter the number 2 =")
    if n1.isnumeric()==True and n2.isnumeric()==True:
        a=int(n1)+int(n2)
        print(a)
    else:
        print("Error in input")

add()