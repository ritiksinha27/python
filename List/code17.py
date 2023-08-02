#Write a Python program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False.

def prime():
    S=input("Enter the numbers =")
    L=S.split(',')
    print(L)
    y=0
    x=0
    D=[]
    for i in L:
        if int(i)==1:
            print("false")
        elif int(i)==2:
            y+=2
            print("true")
        else:
            for j in range(2,int(i)):
                if (int(i) % j)==0:
                    x+=1
                    D.append(j)
        
    if x == 0 and y == 0:
            print("True")
    elif x>0:
            print("False",x,D)    
                
                

prime()