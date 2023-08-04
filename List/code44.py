#  Write a Python program to generate groups of five consecutive numbers in a list.

def cons():
    L=[]
    S=[]
    for i in range(5):
        for j in range(1,6):
            x=int(j+(5*i))
            S.append(x)
        
        L.append(S)
        S=[]
    print(L)
cons()