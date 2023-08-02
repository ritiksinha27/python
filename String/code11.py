S=input("Enter the Sentence =")
L=S.split(' ')
d={}
for i in L:
    if i in d.keys():
        d[i]+=1
    else:
        d[i]=1
print(d)

