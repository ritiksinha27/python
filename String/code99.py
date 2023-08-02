#Write a Python program to split a multi-line string into a list of lines.

def single():
    n=int(input("Enter the number of lines ="))
    L=[]
    for i in range(n):
        S=input("Enter the line =")
        L.append(S)
    print(L)
single()