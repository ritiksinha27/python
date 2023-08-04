# Write a Python program to append a list to the second list.

def second():
    S1=input("Enter the list 1=")
    L1=S1.split(',')
    S2=input("Enter the list 2=")
    L2=S2.split(',')
    L=list(L1 + L2)
    print(L)
second()
    