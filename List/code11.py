#Write a Python function that takes two lists and returns True if they have at least one common member.

L1=[x for x in input("Enter the first list =")]
L2=[x for x in input("Enter the second list =")]
S=[]
for i in L1:
    for j in L2:
        if j==i:
            S.append(j)
if S==[]:
    print("False")
else:
    print(S,"True")