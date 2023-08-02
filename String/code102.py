#Write a Python program to remove punctuation from a given string.
def punc():
    S=input("Enter the string =")
    x=''
    for i in S:
        if i.isalpha()==True or i==' ':
            x+=i
    print(x)

punc()