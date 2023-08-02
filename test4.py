#repeatition in a string

def repeat():
    S=input("Enter the string =")
    d={}
    for i in S:
        if i in d.keys():
            d[i]+=1
        else:
            d[i]=1
    print(d)

repeat()