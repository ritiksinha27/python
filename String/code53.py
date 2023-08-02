#Write a Python program to find the first repeated character in a given string where the index of the first occurrence is smallest.

def repeatindex():
    S=input("Enter the string =")
    d={}
    for i in S:
        if i in d.keys():
            d[i]+=1
        else:
            d[i]=1
    for i in d.keys():
        if d[i] > 1:
            for j in range(len(S)):
                if S[j]==i:
                    print(i,j)
                    break
                
repeatindex()