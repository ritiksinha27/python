#Write a Python program to calculate the difference between the two lists.

def diff():
    
    L1=[x for x in input("Enter the list 1=")]
    L2=[x for x in input("Enter the list 2=")]
    dL1L2=list(set(L1)-set(L2))
    dL2L1=list(set(L2)-set(L1))
    totalL=list(dL1L2 + dL2L1)
    print(totalL)
diff()