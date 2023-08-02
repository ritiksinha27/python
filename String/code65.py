# Write a Python program to find all the common characters in 
# lexicographical order from two given lower case strings. 
#If there are no similar letters print "No common characters".

def lexi():
    s1=input("Enter the 1st string =")
    s2=input("Enter the 2nd string =")
    L=[]
    d={}
    for j in s2:
            if j in s1:
                if j in d.keys():
                    d[j]+=1 
                else:
                    d[j]=1
    f=dict(sorted(d.items()))
    print(d)

lexi()
                doubt 