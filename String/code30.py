#Write a Python program to print the following numbers up to 2 decimal places with a sign.

S=float(input("Enter the number ="))
X="{:.2f}".format(S)
print("+"+X)