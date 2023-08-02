a=int(input('enter the number of times'))
for i in range(a):
    z=('*'*(i+1))
    if (i+1)%2==0:
        print(z.center(a+1,'-'))
    else:
        print(z.center(a,'-'))