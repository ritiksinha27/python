#Write a Python program to insert space before every capital letter appears in a given word.

def space():
    S=input("Enter the string =")
    x=''
    for i in S:
        if i.isupper()==True:
            x+=(' '+i)
        else:
            x+=(i)
    print(x)
space()