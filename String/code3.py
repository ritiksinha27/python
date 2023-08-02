#Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.

a=input("Enter the input = ")
for i in range(len(a)):
    if i!=0 and a[i]==a[0]:
        c= a[0:i] + '%' + a[i+1:]
        print(c)
        
        #Why name space overriding