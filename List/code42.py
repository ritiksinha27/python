#  Write a Python program to find missing and additional values in two lists.
# Sample data : Missing values in second list: b,a,c
# Additional values in second list: g,h

def missing():
    L1=[x for x in input("Enter the list1 =")]
    L2=[x for x in input("Enter the list2 =")]
    # x=[]
    # y=[]
    # for i in L1:
    #     if i not in L2:    
    #         y+=i
    # for j in L2:
    #     if j not in L1:
    #         x+=j
    # print("missing in List 2 =",y)
    # print("additional in list 2=",x)
    y=set(L1).difference(L2)
    x=set(L2).difference(L1)
    print("additional in list 2 = ",x)
    print("missing in List 2 =",y)
    
    
    
    
missing()          