S='google.com'
d={}
for i in S:
    if i in d.keys():
        d[i]+=1
    else:
        d[i]=1
print(d)