x=int(input("Enter 1st number = "))
y=int(input("Enter the 2nd number = "))
print("For addition return 1: \n substraction return 2: \n multiply return 3: \n divide return 4:")
z=int(input("Enter your required operator ="))
if z == 1:
    print(x+y)
elif z==2:
    print(x-y) 
elif z==3:
    print(x*y)
elif z==4:
    print(x/y)
else:
    print("wrong input")