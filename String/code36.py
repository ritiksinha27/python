#Write a Python program to display a number in left, right, and center aligned with a width of 10.

def align():
    n=int(input("Enter the number ="))
    L="{:< 10d}".format(n)
    R="{: 10d}".format(n)
    C="{: ^10d}".format(n)
    print("Left=",L +'\n'+'Right=',R+'\n'+"Center=",C )

align()    
    