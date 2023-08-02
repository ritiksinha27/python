'''Write a Python function to insert a string in the middle of a string. '''

S=input("Enter the string =")
t=input("enter the tag =")
l=int((len(t))/2)
print(t[:l]+S+t[l:])

