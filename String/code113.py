#Write a Python program that returns a string sorted alphabetically by the first character of a given string of words.

def sort():
    S=input("Enter the string =")
    L=S.split(',')
    x=sorted(L)
    y=''
    for i in x:
        y+=(i+ ' ')
    print(y)
sort()