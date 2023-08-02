#Write a Python program to find the first repeated word in a given string.
def repeatword():
    S=input("Enter the sentence =")
    L=S.split(' ')
    d={}
    for i in L:
        if i in d.keys():
            d[i]+=1
        else:
            d[i]=1
    for i in d.keys():
        if d[i] > 1:
            print(i)
            break

repeatword()