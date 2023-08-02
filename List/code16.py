#Write a Python program to generate and print a list of the first and 
# last 5 elements where the values are square numbers
# between 1 and 30 (both included).

def square():
    L=[]
    for i in range(1,31):
        x=i**2
        L.append(x)
    print(L[:5])
    print(L[-5:])
square()