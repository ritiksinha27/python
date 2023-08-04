# #Write a Python program to change the position of every n-th value to the (n+1)th in a list.
# Sample list: [0,1,2,3,4,5]
# Expected Output: [1, 0, 3, 2, 5, 4]
def change():
    from itertools import chain,zip_longest,tee
    L=[x for x in input("Enter the list =")]
    L1,L2=tee(iter(L),2)
    F= list(chain.from_iterable(zip_longest(L[1::2], L[::2])))
    print(list(L1),list(L2),F)

change()

        