#Write a Python program to find the maximum length of 
# consecutive 0's in a given binary string

b='10100100010000'
d={}
n=0
for i in range(len(b)):
    if b[i]=='0':
        if b[i-1]=='1':
            n=1
        if b[i-1]=='0':
            n+=1
print(n)