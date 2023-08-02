S=input("Enter the string =")
l=int(len(S)/4)
if l==1:
    print(S[-1::-1])
else:
    print(S)