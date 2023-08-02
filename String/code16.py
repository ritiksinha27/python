#Write a Python function to get a string made of 4 copies of the last two characters of a specified string

S=input("Enter the string")
print((S[-2::1])*4)