#Write a Python program to generate all sublists of a list.

def sublist():
    import itertools
    L=input("Enter the list =")
    S=[]
    for i in range(len(L)+1):
        F=[list(x) for x in itertools.combinations(L,i)]
        for j in F:
            S.append(j)
    print(S)
sublist()