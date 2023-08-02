# Write a Python program to move all spaces to the front of a given string in a single traversal.

def spaceno():
    S=input("Enter the string =")
    st=''
    ns=[x for x in S if x!=' ' ]
    for i in ns:
        st+=i
    print(st)

spaceno()