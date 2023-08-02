# Write a Python program to reverse a string.

def reverse():
    F=''
    S=input("enter the string =")
    for i in range(-1,-(len(S)+1),-1):
        F+=S[i]
    print(F)

reverse()