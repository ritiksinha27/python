#Write a Python program to remove all consecutive duplicates of a given string.

def remvnxtduplicate():
    S=input("Enter the string =")
    L=''
    for i in range(len(S)-1):
            
            if S[i]==S[i+1] and S[i] not in L:
                L+=S[i]
            if S[i]!=S[i+1]:
                L+=S[i+1]
    print(L)
    
remvnxtduplicate()
    