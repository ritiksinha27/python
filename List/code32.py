#Write a Python program to check whether a list contains a sublist.

def check():
    # L1=[x for x in input("Enter the list  =")]
    # L2=[x for x in input("Enter the sublist  =")]
    # print(L1,L2)
    # x=L2 in L1
    # if x==True:
    #     print("sublist exist")
    # else:
    #     print("Sublist does not exist")
    L1=input("Enter the list  =")
    L2=input("Enter the sublist  =")
    S1=''
    S2=''
    for i in L1:
        if i.isnumeric() == True:
            S1+=str(i)
    for j in L2:
        if j.isnumeric() == True:
            S2+=str(j)
    if S2 in S1:
        print("Yes")
    else:
        print('No')
check()
