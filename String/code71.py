#Write a Python program that concatenates uncommon characters from two strings.

def concat():
    S1=input("Enter the string 1 =")
    S2=input("Enter the string 2 =")
    x=''
    y={}
    
    for i in S1:
        for j in S2:
            if j==i:
                if j not in x:
                    x+=j 
            else:
                if j not in y.keys():
                    y[j]=1
    
    print(x,y)
concat()

uncommon-----SET 