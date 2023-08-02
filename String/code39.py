#Write a Python program to reverse words in a string.

def revwords():
    R=''
    S=input("Enter the string =")
    fS=S.split(' ')
    for i in range(-1,-(len(fS)+1),-1):
        R+=(fS[i]+' ')
    print(R)
revwords()