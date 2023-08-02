S=input("Enter the string =")
c=input("enter the specified character")
for i in range(len(S)):
    if S[i]==c:
        print(S[:i])
    
