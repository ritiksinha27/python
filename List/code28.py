#Write a Python program to find the second largest number in a list.

def secondlarge():
    S=input("Enter the number =")
    L=[int(x) for x in S.split(',')]
    finalL=sorted(L)
    print(finalL[-2])

secondlarge()