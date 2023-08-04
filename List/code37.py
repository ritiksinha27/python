#Write a Python program to find common items in two lists.
def common():
    L1=[x for x in input("Enter the list 1 =")]
    L2=[x for x in input("Enter the list 2 =")]
    x=''
    for i in L1:
        if i in L2 and i not in x:
            x+=i
    for j in L2:
        if j in L1 and j not in x:
            x+=j
    print(x)
common()