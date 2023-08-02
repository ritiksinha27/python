#Write a Python program to calculate the sum of two numbers given as strings. 
# Return the result in the same string representation.

def sum():
    S=input("Enter the number =")
    x=S.split(',')
    try:
        y= int(x[0]) + int(x[1])
        print(y)
    except:
        print("Incorect input")
        
sum()    