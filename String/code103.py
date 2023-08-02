#Write a Python program to replace each character of a word of length 
# five and more with a hash character (#).

def hash():
    S=input("Enter the string =")
    x=''
    L=S.split(' ')
    for i in L:
        if len(i)>=5:
            x+=(len(i)*'#' + ' ' )
        else:
            x+=(i+' ')
    print(x)
hash()