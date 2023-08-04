#Write a Python program to create a list by concatenating a 
# given list with a range from 1 to n.
# Sample list : ['p', 'q']

def concat():
    L=[str(x) for x in input("Enter the list =").split(',')]
    
    n=int(input("enter the range ="))
    # for i in L:
    #     for j in range(1,n+1):
    X=['{}{}'.format(i,j) for j in range(1, n+1) for i in L]
    print(X)            
concat()