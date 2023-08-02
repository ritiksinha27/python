#take user input list ..make it a string and give output.
def lsttostr(L):
    L1=L.split(',')
    S=''
    for i in L1:
        S+=i
    print(S)
    
L=input("Enter the List =")

lsttostr(L)
