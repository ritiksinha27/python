#Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

a=input("Enter the firt string = ")
b=input("Enter the second string = ")
x=b[0] + a[1::] 
y=a[0] + b[1::]
print(x+' '+y)