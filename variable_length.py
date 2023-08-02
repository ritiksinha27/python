'''def abc(*a):
    print(a)

x = abc(1,2,3,'b')

for keyword'''

def abc(*a,**b):
    print(a,b)

x = abc(1,45,'x',a=3,b=44)

