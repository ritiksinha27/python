# Write a Python program to find the longest common sub-string from two given strings.

def longest():
    S1=input("Enter the string 1 =")
    S2=input("Enter the string 2 =")
    x=''
    for i in S1:
        '''for j in S2:
            if j==i:
                if j not in x:
                    x+=j'''
        if i in S2:
            x+=i
                    
                
    print(x)

longest()
regex