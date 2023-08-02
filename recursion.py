def rec(a,i):
    if  i == a:
        print(a)
    else :
        print(i)
        i=i+1
        rec(a,i)
    
a=5
i=0
b=rec(a, i)
