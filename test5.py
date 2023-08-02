#make dict and save 4 data unit as per user;

def dctsave(i,d):
    if i==4:
        print(d)
    else:
        a=input("Enter the key =")
        b=input("Enter the value =")
        i+=1    
        d[a]=b
        dctsave(i,d)
    #print(d)
d={}
dctsave(0,d)