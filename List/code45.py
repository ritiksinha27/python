# Write a Python program to convert a pair of values into a sorted unique array.

def unique():
    L=[(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4),
 (7, 8), (9, 10)]
    L1=[]
    for i in L:
        #/print(i)
        L1.append(i[0])
        L1.append(i[1])
    print(list(set(L1)))
    #s = set(L1)
unique()