#Write a Python program to find the common values that appear in two given strings.

def common():
    S1=input("Enter the string 1 =")
    S2=input("Enter the string 2 =")
    x=''
    for i in S1:
        if i in S2 and i not in x:
            x+=i
    print(x)

common()