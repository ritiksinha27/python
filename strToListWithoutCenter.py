a=int(input('enter the number of times'))
for i in range(a):
    z=('*'*(i+1))
    for j in range(i+1):
        y=(' '*(j+1))
        print(y,z)